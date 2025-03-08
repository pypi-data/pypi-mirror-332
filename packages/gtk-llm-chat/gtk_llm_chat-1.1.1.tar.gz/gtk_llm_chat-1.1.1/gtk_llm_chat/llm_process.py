"""
Manejo simplificado del proceso LLM como subproceso.
"""

from datetime import datetime
from gi.repository import GLib, Gio, GObject


class Message:
    """
    Representa un mensaje
    """
    def __init__(self, content, sender="user", timestamp=None):
        self.content = content
        self.sender = sender
        self.timestamp = timestamp or datetime.now()


class LLMProcess(GObject.Object):
    """
    Maneja el subproceso LLM y emite señales con las respuestas
    """
    __gsignals__ = {
        'response': (GObject.SignalFlags.RUN_LAST, None, (str,)),  # Emite cada token de respuesta
        'model-name': (GObject.SignalFlags.RUN_LAST, None, (str,)),  # Emite el nombre del modelo
        'ready': (GObject.SignalFlags.RUN_LAST, None, ())  # Emite cuando está listo para nueva entrada
    }

    def __init__(self, config=None):
        GObject.Object.__init__(self)
        self.process = None
        self.is_generating = False
        self.launcher = None
        self.config = config or {}
        self.token_queue = []  # Cola para almacenar tokens

    def initialize(self):
        """Inicia el proceso LLM"""
        try:
            if not self.process:
                print("Iniciando proceso LLM...")
                self.launcher = Gio.SubprocessLauncher.new(
                    Gio.SubprocessFlags.STDIN_PIPE |
                    Gio.SubprocessFlags.STDOUT_PIPE |
                    Gio.SubprocessFlags.STDERR_PIPE
                )

                # Construir comando con argumentos
                cmd = ['llm', 'chat']

                # Agregar argumentos básicos
                if self.config.get('cid'):
                    cmd.extend(['--cid', self.config['cid']])
                elif self.config.get('continue_last'):
                    cmd.append('-c')

                if self.config.get('system'):
                    cmd.extend(['-s', self.config['system']])

                if self.config.get('model'):
                    cmd.extend(['-m', self.config['model']])

                # Agregar template y parámetros
                if self.config.get('template'):
                    cmd.extend(['-t', self.config['template']])

                if self.config.get('params'):
                    for param in self.config['params']:
                        cmd.extend(['-p', param[0], param[1]])

                # Agregar opciones del modelo
                if self.config.get('options'):
                    for opt in self.config['options']:
                        cmd.extend(['-o', opt[0], opt[1]])

                try:
                    print(f"Ejecutando comando: {' '.join(cmd)}")
                    self.process = self.launcher.spawnv(cmd)
                except GLib.Error as e:
                    print(f"Error al iniciar LLM: {str(e)}")
                    return

                # Configurar streams
                self.stdin = self.process.get_stdin_pipe()
                self.stdout = self.process.get_stdout_pipe()

                # Leer mensaje inicial
                self.stdout.read_bytes_async(
                    4096,
                    GLib.PRIORITY_DEFAULT,
                    None,
                    self._handle_initial_output
                )
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    def send_message(self, messages):
        """Ejecuta el LLM con los mensajes dados"""
        if not self.process:
            self.initialize()
            return

        try:
            self.is_generating = True

            # Enviar solo el último mensaje
            if messages:
                # Enviar mensaje sin formateo especial
                message = messages[-1]
                stdin_data = f"{message.sender}: {message.content}\n"
                if "\n" in message.content:
                    stdin_data = f"!multi\n{message.sender}: {message.content}\n!end\n"
                self.stdin.write_bytes(GLib.Bytes(stdin_data.encode("utf-8")))

            self._read_response(self._emit_response)

        except Exception as e:
            print(f"Error ejecutando LLM: {e}")
            self.is_generating = False

    def _handle_initial_output(self, stdout, result):
        """Maneja la salida inicial del proceso"""
        try:
            bytes_read = stdout.read_bytes_finish(result)
            if bytes_read:
                text = bytes_read.get_data().decode('utf-8')
                # Extraer el nombre del modelo si está presente (con o sin espacio)
                if "Chatting with" in text:
                    model_name = text.split("Chatting with")[1].split("\n")[0].strip()
                    print(f"Usando modelo: {model_name}")
                    self.emit('model-name', model_name)
                
                # Continuar leyendo la respuesta
                self._read_response(self._emit_response)
                
        except Exception as e:
            print(f"Error leyendo salida inicial: {e}")

    def _read_response(self, callback, accumulated=""):
        """Lee la respuesta del LLM de forma incremental"""
        # Leer bytes de forma asíncrona
        self.stdout.read_bytes_async(
            1024,
            GLib.PRIORITY_DEFAULT,
            None,
            self._handle_response,
            callback
        )

    def _emit_response(self, text):
        """Emite la señal de respuesta"""
        # Agregar token a la cola
        self.token_queue.append(text)
        # Emitir señal con el token
        self.emit('response', text)

    def _handle_response(self, stdout, result, user_data):
        """Maneja cada token de la respuesta"""
        callback = user_data
        try:
            try:
                bytes_read = stdout.read_bytes_finish(result)
                if bytes_read:
                    text = bytes_read.get_data().decode('utf-8')
                    
                    # Detectar si el modelo está listo para nueva entrada
                    if text.strip() == ">" or text.endswith("\n> ") or text.endswith("> "):
                        self.emit('ready')
                        print("Modelo listo para nueva entrada")
                    else:
                        # Emitir el token recibido
                        callback(text)
                        print(text, end="", flush=True)
                    
                    self._read_response(callback)
                else:
                    self.is_generating = False
            except Gio.Error as e:
                print(f"Error de GIO al leer respuesta: {e}")
                self.is_generating = False
        except Exception as e:
            print(f"Error leyendo respuesta: {e}")
            self.is_generating = False

    def cancel(self):
        """Cancela la generación actual"""
        self.is_generating = False
        if self.process:
            self.process.force_exit()
            self.is_generating = False
            try:
                self.stdin.close()
            except Exception:
                pass
            self.token_queue.clear()  # Limpiar la cola de tokens


GObject.type_register(LLMProcess)
