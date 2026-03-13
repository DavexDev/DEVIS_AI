# Flutter — Manejo de Estado

## Ejecutar en Web

```bash
flutter run -d chrome
```

> `setState`, `Provider` y `Riverpod` funcionan exactamente igual en Flutter Web. No hay diferencias de API.

## setState — Estado local (StatefulWidget)

```dart
class ContadorWidget extends StatefulWidget {
  const ContadorWidget({super.key});
  @override
  State<ContadorWidget> createState() => _ContadorWidgetState();
}

class _ContadorWidgetState extends State<ContadorWidget> {
  int _contador = 0;

  void _incrementar() {
    setState(() {
      _contador++;   // setState reconstruye el widget
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text('Contador: $_contador', style: const TextStyle(fontSize: 24)),
        ElevatedButton(
          onPressed: _incrementar,
          child: const Text('Incrementar'),
        ),
      ],
    );
  }
}
```

## Provider — Estado compartido entre pantallas

```yaml
# pubspec.yaml
dependencies:
  provider: ^6.1.0
```

```dart
// 1. Modelo (ChangeNotifier)
import 'package:flutter/foundation.dart';

class ContadorModel extends ChangeNotifier {
  int _valor = 0;
  int get valor => _valor;

  void incrementar() {
    _valor++;
    notifyListeners();   // notifica a todos los widgets que escuchan
  }

  void resetear() {
    _valor = 0;
    notifyListeners();
  }
}
```

```dart
// 2. Registrar el provider en main.dart
import 'package:provider/provider.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => ContadorModel(),
      child: const MyApp(),
    ),
  );
}
```

```dart
// 3. Leer y escribir desde cualquier widget
class PantallaContador extends StatelessWidget {
  const PantallaContador({super.key});

  @override
  Widget build(BuildContext context) {
    // watch: reconstruye widget al cambiar
    final contador = context.watch<ContadorModel>();

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Valor: ${contador.valor}', style: const TextStyle(fontSize: 28)),
            ElevatedButton(
              // read: solo accede sin escuchar (dentro de callbacks)
              onPressed: () => context.read<ContadorModel>().incrementar(),
              child: const Text('Sumar'),
            ),
            TextButton(
              onPressed: () => context.read<ContadorModel>().resetear(),
              child: const Text('Resetear'),
            ),
          ],
        ),
      ),
    );
  }
}
```

## Riverpod — Estado moderno y testeable

```yaml
# pubspec.yaml
dependencies:
  flutter_riverpod: ^2.5.0
```

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';

// 1. Definir provider global
final contadorProvider = StateNotifierProvider<ContadorNotifier, int>(
  (ref) => ContadorNotifier(),
);

class ContadorNotifier extends StateNotifier<int> {
  ContadorNotifier() : super(0);   // estado inicial = 0

  void incrementar() => state++;
  void resetear()    => state = 0;
}
```

```dart
// 2. Envolver la app con ProviderScope
void main() {
  runApp(const ProviderScope(child: MyApp()));
}
```

```dart
// 3. Usar en widgets (ConsumerWidget)
class PantallaRiverpod extends ConsumerWidget {
  const PantallaRiverpod({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final valor = ref.watch(contadorProvider);

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Valor: $valor', style: const TextStyle(fontSize: 28)),
            ElevatedButton(
              onPressed: () => ref.read(contadorProvider.notifier).incrementar(),
              child: const Text('Sumar'),
            ),
          ],
        ),
      ),
    );
  }
}
```

## Comparación de soluciones

| Solución   | Alcance          | Complejidad | Recomendado para                |
| ---------- | ---------------- | ----------- | ------------------------------- |
| `setState` | Local (widget)   | Baja        | UI simple, un solo widget       |
| `Provider` | Global / árbol   | Media       | Apps medianas, equipos pequeños |
| `Riverpod` | Global / modular | Media-Alta  | Apps grandes, código testeable  |
