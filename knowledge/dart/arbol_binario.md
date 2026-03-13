# Dart — Árbol Binario de Búsqueda (BST)

## Implementación completa

```dart
class NodoBST<T extends Comparable<T>> {
  T dato;
  NodoBST<T>? izquierdo;
  NodoBST<T>? derecho;

  NodoBST(this.dato);
}

class ArbolBST<T extends Comparable<T>> {
  NodoBST<T>? raiz;

  // ── Insertar ────────────────────────────────────────────────
  void insertar(T dato) {
    raiz = _insertarRec(raiz, dato);
  }

  NodoBST<T> _insertarRec(NodoBST<T>? nodo, T dato) {
    if (nodo == null) return NodoBST(dato);
    if (dato.compareTo(nodo.dato) < 0) {
      nodo.izquierdo = _insertarRec(nodo.izquierdo, dato);
    } else if (dato.compareTo(nodo.dato) > 0) {
      nodo.derecho = _insertarRec(nodo.derecho, dato);
    }
    // Si dato == nodo.dato, no insertamos duplicados
    return nodo;
  }

  // ── Buscar ──────────────────────────────────────────────────
  bool contiene(T dato) => _buscarRec(raiz, dato);

  bool _buscarRec(NodoBST<T>? nodo, T dato) {
    if (nodo == null) return false;
    final cmp = dato.compareTo(nodo.dato);
    if (cmp == 0) return true;
    if (cmp < 0) return _buscarRec(nodo.izquierdo, dato);
    return _buscarRec(nodo.derecho, dato);
  }

  // ── Eliminar ─────────────────────────────────────────────────
  void eliminar(T dato) {
    raiz = _eliminarRec(raiz, dato);
  }

  NodoBST<T>? _eliminarRec(NodoBST<T>? nodo, T dato) {
    if (nodo == null) return null;
    final cmp = dato.compareTo(nodo.dato);
    if (cmp < 0) {
      nodo.izquierdo = _eliminarRec(nodo.izquierdo, dato);
    } else if (cmp > 0) {
      nodo.derecho = _eliminarRec(nodo.derecho, dato);
    } else {
      // Nodo encontrado
      if (nodo.izquierdo == null) return nodo.derecho;
      if (nodo.derecho == null) return nodo.izquierdo;
      // Tiene dos hijos: reemplazar con el sucesor (mínimo del subárbol derecho)
      final sucesor = _minimo(nodo.derecho!);
      nodo.dato = sucesor.dato;
      nodo.derecho = _eliminarRec(nodo.derecho, sucesor.dato);
    }
    return nodo;
  }

  NodoBST<T> _minimo(NodoBST<T> nodo) {
    while (nodo.izquierdo != null) {
      nodo = nodo.izquierdo!;
    }
    return nodo;
  }

  // ── Recorrido inorder (da valores ordenados en BST) ──────────
  List<T> inorder() {
    final resultado = <T>[];
    _inorderRec(raiz, resultado);
    return resultado;
  }

  void _inorderRec(NodoBST<T>? nodo, List<T> resultado) {
    if (nodo == null) return;
    _inorderRec(nodo.izquierdo, resultado);
    resultado.add(nodo.dato);
    _inorderRec(nodo.derecho, resultado);
  }
}
```

## Ejemplo de uso

```dart
void main() {
  final arbol = ArbolBST<int>();

  for (final v in [50, 30, 70, 20, 40, 60, 80]) {
    arbol.insertar(v);
  }

  print(arbol.inorder());     // [20, 30, 40, 50, 60, 70, 80]
  print(arbol.contiene(40));  // true
  print(arbol.contiene(99));  // false

  arbol.eliminar(30);
  print(arbol.inorder());     // [20, 40, 50, 60, 70, 80]
}
```

## Propiedad BST

```
        50
       /  \
      30   70
     / \   / \
    20  40 60  80
```

- Subárbol izquierdo: todos los valores < nodo
- Subárbol derecho: todos los valores > nodo

## Complejidad

| Operación | Caso promedio | Peor caso (degenerado) |
| --------- | ------------- | ---------------------- |
| Insertar  | O(log n)      | O(n)                   |
| Buscar    | O(log n)      | O(n)                   |
| Eliminar  | O(log n)      | O(n)                   |

## Tags

`dart` `estructuras-datos` `arbol` `bst` `arbol-binario-busqueda` `flutter`
