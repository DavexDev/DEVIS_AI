# Dart — Colas (Queue)

## Implementación con lista enlazada

```dart
class Nodo<T> {
  T dato;
  Nodo<T>? siguiente;
  Nodo(this.dato);
}

/// Cola FIFO — First In, First Out
class Cola<T> {
  Nodo<T>? _frente;
  Nodo<T>? _final;
  int _longitud = 0;

  int get longitud => _longitud;
  bool get estaVacia => _frente == null;

  // Ver el frente sin eliminar — O(1)
  T front() {
    if (estaVacia) throw StateError('La cola está vacía');
    return _frente!.dato;
  }

  // Encolar — O(1)
  void enqueue(T dato) {
    final nuevo = Nodo(dato);
    if (_final == null) {
      _frente = _final = nuevo;
    } else {
      _final!.siguiente = nuevo;
      _final = nuevo;
    }
    _longitud++;
  }

  // Desencolar — O(1)
  T dequeue() {
    if (estaVacia) throw StateError('La cola está vacía');
    final dato = _frente!.dato;
    _frente = _frente!.siguiente;
    if (_frente == null) _final = null;
    _longitud--;
    return dato;
  }

  // Imprimir de frente a final
  void imprimir() {
    Nodo<T>? actual = _frente;
    final buffer = StringBuffer('FRENTE → ');
    while (actual != null) {
      buffer.write('${actual.dato}');
      if (actual.siguiente != null) buffer.write(' → ');
      actual = actual.siguiente;
    }
    buffer.write(' → FINAL');
    print(buffer.toString());
  }
}
```

## Implementación con Queue de Dart

```dart
import 'dart:collection';

void main() {
  // Usar la Queue nativa de Dart
  final cola = Queue<int>();

  cola.add(10);       // enqueue al final
  cola.add(20);
  cola.add(30);

  print(cola.first);       // 10 — ver frente
  print(cola.removeFirst());  // 10 — dequeue
  print(cola.removeLast());   // 30 — quitar del final
}
```

## Ejemplo de uso

```dart
void main() {
  final cola = Cola<String>();

  cola.enqueue('Tarea 1');
  cola.enqueue('Tarea 2');
  cola.enqueue('Tarea 3');

  cola.imprimir();
  // FRENTE → Tarea 1 → Tarea 2 → Tarea 3 → FINAL

  print(cola.dequeue());   // Tarea 1
  print(cola.dequeue());   // Tarea 2
  print(cola.longitud);    // 1
}
```

## Cola de Prioridad (simple)

```dart
import 'dart:collection';

// Los elementos con menor valor tienen mayor prioridad
final colaPrioridad = SplayTreeMap<int, String>();

colaPrioridad[3] = 'Baja prioridad';
colaPrioridad[1] = 'Alta prioridad';
colaPrioridad[2] = 'Media prioridad';

// Procesar en orden de prioridad
for (final entry in colaPrioridad.entries) {
  print('Prioridad ${entry.key}: ${entry.value}');
}
```

## Aplicaciones

- Sistemas de turnos / tickets
- BFS (Búsqueda en amplitud en grafos y árboles)
- Impresoras, colas de procesos del SO
- Stream de eventos en Flutter

## Complejidad

| Operación | Complejidad |
| --------- | ----------- |
| `enqueue` | O(1)        |
| `dequeue` | O(1)        |
| `front`   | O(1)        |

## Tags

`dart` `estructuras-datos` `cola` `queue` `fifo` `flutter`
