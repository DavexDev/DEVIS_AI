# Flutter — App Básica con Contador (StatefulWidget)

## Descripción

App con contador que se incrementa y decrementa usando dos `FloatingActionButton`.
Muestra el uso de `StatefulWidget`, `setState`, widgets personalizados y estructura base de `MaterialApp`.

## Código — `main.dart`

```dart
import 'package:flutter/material.dart';
import 'saludo.dart';   // widget personalizado externo

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Clase 1'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() => _counter++);
  }

  void _decrementCounter() {
    setState(() => _counter--);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: Text(widget.title),   // accede al campo del StatefulWidget
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            // Texto con estilo explícito
            const Text(
              'Hola mundo',
              style: TextStyle(
                fontSize: 18,
                color: Colors.red,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),

            // Widget personalizado importado
            const SaludoWidget(nombre: 'Flutter'),

            const Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [Text('HOLA MUNDO FLUTTER')],
            ),

            const Text('CLASE 1 FLUTTER:'),

            // Muestra el valor del contador con estilo del tema
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),

      // Dos FABs en un Row: decrementar e incrementar
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          FloatingActionButton(
            onPressed: _decrementCounter,
            tooltip: 'Decrement',
            child: const Icon(Icons.remove),
          ),
          const SizedBox(width: 16),
          FloatingActionButton(
            onPressed: _incrementCounter,
            tooltip: 'Increment',
            child: const Icon(Icons.add),
          ),
        ],
      ),
    );
  }
}
```

## Conceptos clave

### StatefulWidget vs StatelessWidget

|                | StatelessWidget | StatefulWidget |
| -------------- | --------------- | -------------- |
| Estado mutable | ❌ No           | ✅ Sí          |
| `setState`     | ❌ No           | ✅ Sí          |
| Cuándo usar    | UI fija         | UI que cambia  |

### setState

```dart
setState(() {
  _counter++;   // cualquier cambio de variable aquí redibuja el widget
});
```

### Acceder al widget desde el State

```dart
widget.title   // lee propiedades del StatefulWidget desde _State
```

### Tema Material 3

```dart
theme: ThemeData(
  colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
  useMaterial3: true,
),
```

## Tags

`flutter` `statefulwidget` `setstate` `contador` `floatingactionbutton` `material3`
