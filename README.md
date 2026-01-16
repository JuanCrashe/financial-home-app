# Finanzas Habitacional - Sistema de Gestión

Una aplicación web moderna para la administración financiera de conjuntos residenciales y propiedad horizontal. Permite gestionar ingresos, egresos, presupuestos y reportes de manera transparente y eficiente.

## 🚀 Características

- **Landing Page**: Página de presentación pública con planes y características.
- **Autenticación**: Login de usuarios (Administradores).
- **Dashboard**: Resumen financiero en tiempo real (Ingresos vs Egresos).
- **Gestión de Ingresos**: Registro de cuotas de mantenimiento, reservas y otros cobros.
- **Control de Egresos**: Registro de gastos por categoría y proveedores.
- **Presupuestos**: Visualización de ejecución presupuestal con barras de progreso.
- **Reportes**: Centro de reportes financieros y gráficos.
- **Diseño Responsive**: Interfaz adaptada a móviles y escritorio (Bootstrap 5).

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3, Flask.
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
- **Framework CSS**: Bootstrap 5.3.
- **Iconos**: Bootstrap Icons.
- **Tipografía**: Google Fonts (Inter).

## 📋 Pre-requisitos

- Python 3.8 o superior.
- Navegador web moderno.

## 🔧 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio** (o descargar los archivos):

    ```bash
    git clone <url-del-repositorio>
    cd habitacional-app
    ```

2.  **Crear y activar un entorno virtual**:

    - _Windows (PowerShell)_:
      ```powershell
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - _macOS / Linux_:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Instalar dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración (Opcional)**:
    - El archivo `config.py` contiene la configuración básica (Secret Key). Puedes modificarlo según tus necesidades.

## ▶️ Ejecución

1.  Asegúrate de tener el entorno virtual activado.
2.  Ejecuta la aplicación:
    ```bash
    python app.py
    ```
3.  Abre tu navegador y visita:
    ```
    http://127.0.0.1:5000
    ```

## 📂 Estructura del Proyecto

```text
habitacional-app/
├── app.py                  # Servidor Flask (Rutas principales)
├── config.py               # Configuración de la app
├── requirements.txt        # Dependencias de Python
├── static/                 # Archivos estáticos (CSS, JS)
│   ├── css/
│   └── js/
└── templates/              # Plantillas HTML (Jinja2)
    ├── base.html           # Layout base (Navbar, Sidebar)
    ├── index.html          # Landing Page
    ├── auth/               # Páginas de autenticación
    └── dashboard/          # Módulos del sistema (Ingresos, Egresos, etc.)
```

## 👥 Contribución

Si deseas contribuir, por favor abre un Pull Request o reporta issues en el repositorio.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
