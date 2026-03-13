# Flutter — Widgets Personalizados (StatelessWidget con parámetros)

## Ejecutar en Web

```bash
flutter run -d chrome
```

> Los widgets personalizados funcionan igual en web, móvil y desktop. No requieren ajustes.

## Descripción

Cómo crear un `StatelessWidget` reutilizable que recibe parámetros desde el exterior.

## Código — `saludo.dart`

```dart
import 'package:flutter/material.dart';

class SaludoWidget extends StatelessWidget {
  const SaludoWidget({super.key, required this.nombre});

  final String nombre;   // parámetro obligatorio

  @override
  Widget build(BuildContext context) {
    return Text('Hola $nombre');
  }
}
```

## Cómo usarlo en otro archivo

```dart
import 'saludo.dart';

// Dentro del método build de cualquier widget:
const SaludoWidget(nombre: 'Flutter')
const SaludoWidget(nombre: 'DEVIS')
```

## Widget con múltiples parámetros

```dart
class TarjetaUsuario extends StatelessWidget {
  const TarjetaUsuario({
    super.key,
    required this.nombre,
    required this.edad,
    this.activo = true,         // parámetro opcional con valor por defecto
    this.color = Colors.blue,
  });

  final String nombre;
  final int edad;
  final bool activo;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Card(
      color: activo ? color : Colors.grey,
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          children: [
            Text(nombre, style: const TextStyle(fontWeight: FontWeight.bold)),
            Text('Edad: $edad'),
            Text(activo ? 'Activo' : 'Inactivo'),
          ],
        ),
      ),
    );
  }
}

// Uso:
TarjetaUsuario(nombre: 'Ana', edad: 25)
TarjetaUsuario(nombre: 'Luis', edad: 30, activo: false, color: Colors.green)
```

## Widget que recibe otro widget como parámetro (child)

```dart
class ContenedorEstilizado extends StatelessWidget {
  const ContenedorEstilizado({super.key, required this.child});

  final Widget child;   // recibe un widget hijo

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.blue.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.blue),
      ),
      child: child,
    );
  }
}

// Uso:
ContenedorEstilizado(
  child: Text('Contenido personalizado'),
)
```

## Conceptos clave

### required vs opcional

```dart
const MyWidget({
  super.key,
  required this.titulo,   // obligatorio: se debe pasar siempre
  this.subtitulo = '',    // opcional: tiene valor por defecto
  this.icono,             // opcional: puede ser null
});
```

### Cuándo usar StatelessWidget vs StatefulWidget

| Criterio                     | StatelessWidget | StatefulWidget |
| ---------------------------- | --------------- | -------------- |
| Tiene estado interno mutable | ❌              | ✅             |
| Solo muestra datos pasados   | ✅              | ✅             |
| Necesita `setState`          | ❌              | ✅             |
| Más performante              | ✅              | —              |

## Tags

`flutter` `statelesswidget` `widget-personalizado` `parametros` `reutilizable` `dart`
