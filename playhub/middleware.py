import time
import logging

# Configuramos un logger básico para ver los resultados en la consola
logger = logging.getLogger(__name__)


class PlayHubMetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # --- ANTES de la vista ---
        start_time = time.time()

        response = self.get_response(request)

        # --- DESPUÉS de la vista ---
        duration = time.time() - start_time

        usuario = request.user.username if request.user.is_authenticated else "Anónimo"
        metodo = request.method
        ruta = request.path

        # Imprime en la terminal de VS Code la métrica
        print(f"\n[MÉTRICA] {metodo} {ruta} | Usuario: {usuario} | Tiempo: {duration:.4f}s")

        return response