# Dart — Pilas (Stack)

## Implementación con lista enlazada

```dart
class Nodo<T> {
  T dato;
  Nodo<T>? siguiente;
  Nodo(this.dato);
}

/// Pila LIFO — Last In, First Out
class Pila<T> {
  Nodo<T>? _cima;
  int _longitud = 0;

  int get longitud => _longitud;
  bool get estaVacia => _cima == null;

  // Ver el tope sin eliminar — O(1)
  T peek() {
    if (estaVacia) throw StateError('La pila está vacía');
    return _cima!.dato;
  }

  // Apilar — O(1)
  void push(T dato) {
    final nuevo = Nodo(dato);
    nuevo.siguiente = _cima;
    _cima = nuevo;
    _longitud++;
  }

  // Desapilar — O(1)
  T pop() {
    if (estaVacia) throw StateError('La pila está vacía');
    final dato = _cima!.dato;
    _cima = _cima!.siguiente;
    _longitud--;
    return dato;
  }

  // Imprimir desde la cima
  void imprimir() {
    Nodo<T>? actual = _cima;
    print('CIMA ↓');
    while (actual != null) {
      print('  ${actual.dato}');
      actual = actual.siguiente;
    }
    print('─────');
  }
}
```

## Implementación con List de Dart (más simple)

```dart
class PilaLista<T> {
  final List<T> _datos = [];

  bool get estaVacia => _datos.isEmpty;
  int get longitud => _datos.length;

  void push(T dato) => _datos.add(dato);
  T pop() => _datos.removeLast();
  T peek() => _datos.last;
}
```

## Ejemplo de uso

```dart
void main() {
  final pila = Pila<int>();

  pila.push(10);
  pila.push(20);
  pila.push(30);

  pila.imprimir();
  // CIMA ↓
  //   30
  //   20
  //   10
  // ─────

  print(pila.peek());  // 30 — no elimina
  print(pila.pop());   // 30 — elimina
  print(pila.pop());   // 20
  print(pila.longitud);// 1
}
```

## Aplicaciones en Flutter / Dart

```dart
// Navigator usa internamente una pila de rutas
Navigator.push(context, ...)   // push a la pila
Navigator.pop(context)         // pop de la pila

// Deshacer/rehacer acciones en editores
// Evaluación de expresiones matemáticas
// Backtracking (laberintos, sudoku)
```

## Complejidad

| Operación | Complejidad |
| --------- | ----------- |
| `push`    | O(1)        |
| `pop`     | O(1)        |
| `peek`    | O(1)        |

## Tags

`dart` `estructuras-datos` `pila` `stack` `lifo` `flutter`
