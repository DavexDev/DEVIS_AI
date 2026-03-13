# Dart — Listas Enlazadas

## Lista Simplemente Enlazada

```dart
/// Nodo de la lista enlazada
class Nodo<T> {
  T dato;
  Nodo<T>? siguiente;

  Nodo(this.dato);
}

/// Lista simplemente enlazada
class ListaEnlazada<T> {
  Nodo<T>? cabeza;
  int _longitud = 0;

  int get longitud => _longitud;
  bool get estaVacia => cabeza == null;

  // Insertar al inicio — O(1)
  void insertarAlInicio(T dato) {
    final nuevo = Nodo(dato);
    nuevo.siguiente = cabeza;
    cabeza = nuevo;
    _longitud++;
  }

  // Insertar al final — O(n)
  void insertarAlFinal(T dato) {
    final nuevo = Nodo(dato);
    if (cabeza == null) {
      cabeza = nuevo;
    } else {
      Nodo<T> actual = cabeza!;
      while (actual.siguiente != null) {
        actual = actual.siguiente!;
      }
      actual.siguiente = nuevo;
    }
    _longitud++;
  }

  // Eliminar por valor — O(n)
  bool eliminar(T dato) {
    if (cabeza == null) return false;
    if (cabeza!.dato == dato) {
      cabeza = cabeza!.siguiente;
      _longitud--;
      return true;
    }
    Nodo<T> actual = cabeza!;
    while (actual.siguiente != null) {
      if (actual.siguiente!.dato == dato) {
        actual.siguiente = actual.siguiente!.siguiente;
        _longitud--;
        return true;
      }
      actual = actual.siguiente!;
    }
    return false;
  }

  // Buscar — O(n)
  bool contiene(T dato) {
    Nodo<T>? actual = cabeza;
    while (actual != null) {
      if (actual.dato == dato) return true;
      actual = actual.siguiente;
    }
    return false;
  }

  // Imprimir — O(n)
  void imprimir() {
    Nodo<T>? actual = cabeza;
    final buffer = StringBuffer();
    while (actual != null) {
      buffer.write('${actual.dato}');
      if (actual.siguiente != null) buffer.write(' → ');
      actual = actual.siguiente;
    }
    buffer.write(' → null');
    print(buffer.toString());
  }
}
```

## Lista Doblemente Enlazada

```dart
class NodoDoble<T> {
  T dato;
  NodoDoble<T>? siguiente;
  NodoDoble<T>? anterior;

  NodoDoble(this.dato);
}

class ListaDoble<T> {
  NodoDoble<T>? cabeza;
  NodoDoble<T>? cola;
  int _longitud = 0;

  int get longitud => _longitud;

  void insertarAlFinal(T dato) {
    final nuevo = NodoDoble(dato);
    if (cola == null) {
      cabeza = cola = nuevo;
    } else {
      nuevo.anterior = cola;
      cola!.siguiente = nuevo;
      cola = nuevo;
    }
    _longitud++;
  }

  void insertarAlInicio(T dato) {
    final nuevo = NodoDoble(dato);
    if (cabeza == null) {
      cabeza = cola = nuevo;
    } else {
      nuevo.siguiente = cabeza;
      cabeza!.anterior = nuevo;
      cabeza = nuevo;
    }
    _longitud++;
  }
}
```

## Ejemplo de uso

```dart
void main() {
  final lista = ListaEnlazada<int>();
  lista.insertarAlFinal(10);
  lista.insertarAlFinal(20);
  lista.insertarAlFinal(30);
  lista.insertarAlInicio(5);

  lista.imprimir();             // 5 → 10 → 20 → 30 → null
  print(lista.contiene(20));    // true
  lista.eliminar(20);
  lista.imprimir();             // 5 → 10 → 30 → null
}
```

## Complejidad

| Operación       | Lista Simple | Lista Doble                |
| --------------- | ------------ | -------------------------- |
| Insertar inicio | O(1)         | O(1)                       |
| Insertar final  | O(n)         | O(1) con puntero cola      |
| Eliminar        | O(n)         | O(n) buscar, O(1) eliminar |
| Buscar          | O(n)         | O(n)                       |

## Tags

`dart` `estructuras-datos` `lista-enlazada` `nodo` `flutter`
