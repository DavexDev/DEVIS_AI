# Flutter Web — Guía de Referencia

## Requisitos previos

```bash
# Habilitar soporte web (solo la primera vez)
flutter config --enable-web

# Verificar que Chrome aparece como dispositivo disponible
flutter devices
# Salida esperada:
#   Chrome (web) • chrome • web-javascript • ...
```

## Crear y correr un proyecto web

```dart
// 1. Crear proyecto
flutter create mi_app
cd mi_app

// 2. Correr en Chrome con hot reload
flutter run -d chrome

// 3. Correr en modo server (accesible desde la red local)
flutter run -d web-server --web-port 8080
// Abrir: http://localhost:8080
```

## Compilar para producción

```bash
flutter build web
# Archivos generados en: build/web/

# Servir localmente para probar
cd build/web
python3 -m http.server 8080
# Abrir: http://localhost:8080
```

## Estructura de build/web/

```
build/web/
├── index.html          # punto de entrada
├── main.dart.js        # código Dart compilado
├── flutter.js
├── flutter_service_worker.js
└── assets/
    └── ...             # fuentes, imágenes, etc.
```

## Responsive Design

```dart
import 'package:flutter/material.dart';

// Con LayoutBuilder
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth > 800) {
      return DesktopLayout();
    } else {
      return MobileLayout();
    }
  },
)

// Con MediaQuery
double ancho = MediaQuery.of(context).size.width;
bool esEscritorio = ancho > 800;
```

## Navegación recomendada para Web (go_router)

```yaml
# pubspec.yaml
dependencies:
  go_router: ^14.0.0
```

```dart
import 'package:go_router/go_router.dart';

final router = GoRouter(
  routes: [
    GoRoute(path: '/',     builder: (ctx, s) => HomePage()),
    GoRoute(path: '/detalle/:id', builder: (ctx, s) {
      final id = s.pathParameters['id']!;
      return DetallePage(id: id);
    }),
  ],
);

// Navegar
context.go('/detalle/42');   // reemplaza la URL del navegador
context.push('/detalle/42'); // apila (botón atrás funciona)
```

> `go_router` sincroniza las rutas con la barra de direcciones del navegador,
> lo que permite bookmarks, compartir URL y navegación con botón atrás del browser.

## Limitaciones en Flutter Web

| Función                  | Web | Nota                                      |
|--------------------------|-----|-------------------------------------------|
| `dart:io` (File, Socket) | ❌  | Usar `http` o `dio` para peticiones       |
| Bluetooth / NFC          | ❌  | No disponibles en navegador               |
| SQLite (sqflite)         | ❌  | Usar `shared_preferences` o IndexedDB     |
| `WillPopScope`           | ⚠️  | Reemplazar con `PopScope` (Flutter 3.12+) |
| Notificaciones push      | ⚠️  | Requiere configuración especial de PWA    |
| `path_provider`          | ❌  | No aplica en web                          |

## PopScope (reemplaza WillPopScope en Flutter 3.12+)

```dart
// ❌ Evitar en web:
// WillPopScope(onWillPop: ..., child: ...)

// ✅ Usar:
PopScope(
  canPop: false,
  onPopInvokedWithResult: (bool didPop, dynamic result) {
    if (!didPop) {
      // lógica antes de salir
    }
  },
  child: Scaffold(...),
)
```

## Buenas prácticas en Flutter Web

```dart
// Cursor en elementos interactivos (hover)
MouseRegion(
  cursor: SystemMouseCursors.click,
  child: GestureDetector(
    onTap: () {},
    child: Text('Haz clic aquí'),
  ),
)

// SelectionArea — permite seleccionar texto con el mouse
SelectionArea(
  child: Column(children: [Text('Texto seleccionable')]),
)
```

## Comandos útiles

```bash
flutter doctor -v                  # verificar instalación
flutter devices                    # listar dispositivos/navegadores
flutter run -d chrome              # correr en Chrome
flutter run -d web-server          # correr como servidor web
flutter build web --release        # build optimizado
flutter build web --profile        # build de perfil (diagnóstico)
flutter clean && flutter pub get   # limpiar y reinstalar dependencias
```
