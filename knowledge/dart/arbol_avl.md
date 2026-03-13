# Dart — Árbol AVL (Auto-balanceado)

## Implementación completa

```dart
class NodoAVL<T extends Comparable<T>> {
  T dato;
  NodoAVL<T>? izquierdo;
  NodoAVL<T>? derecho;
  int altura;

  NodoAVL(this.dato) : altura = 1;
}

class ArbolAVL<T extends Comparable<T>> {
  NodoAVL<T>? raiz;

  // ── Utilidades ───────────────────────────────────────────────
  int _altura(NodoAVL<T>? n) => n?.altura ?? 0;

  int _factorBalance(NodoAVL<T>? n) {
    if (n == null) return 0;
    return _altura(n.izquierdo) - _altura(n.derecho);
  }

  void _actualizarAltura(NodoAVL<T> n) {
    n.altura = 1 + [_altura(n.izquierdo), _altura(n.derecho)]
        .reduce((a, b) => a > b ? a : b);
  }

  // ── Rotaciones ───────────────────────────────────────────────

  // Rotación simple derecha (caso izquierda-izquierda)
  NodoAVL<T> _rotarDerecha(NodoAVL<T> y) {
    final x = y.izquierdo!;
    final T2 = x.derecho;
    x.derecho = y;
    y.izquierdo = T2;
    _actualizarAltura(y);
    _actualizarAltura(x);
    return x;
  }

  // Rotación simple izquierda (caso derecha-derecha)
  NodoAVL<T> _rotarIzquierda(NodoAVL<T> x) {
    final y = x.derecho!;
    final T2 = y.izquierdo;
    y.izquierdo = x;
    x.derecho = T2;
    _actualizarAltura(x);
    _actualizarAltura(y);
    return y;
  }

  // ── Balancear ────────────────────────────────────────────────
  NodoAVL<T> _balancear(NodoAVL<T> nodo) {
    _actualizarAltura(nodo);
    final fb = _factorBalance(nodo);

    // Caso Izquierda-Izquierda
    if (fb > 1 && _factorBalance(nodo.izquierdo) >= 0) {
      return _rotarDerecha(nodo);
    }
    // Caso Izquierda-Derecha
    if (fb > 1 && _factorBalance(nodo.izquierdo) < 0) {
      nodo.izquierdo = _rotarIzquierda(nodo.izquierdo!);
      return _rotarDerecha(nodo);
    }
    // Caso Derecha-Derecha
    if (fb < -1 && _factorBalance(nodo.derecho) <= 0) {
      return _rotarIzquierda(nodo);
    }
    // Caso Derecha-Izquierda
    if (fb < -1 && _factorBalance(nodo.derecho) > 0) {
      nodo.derecho = _rotarDerecha(nodo.derecho!);
      return _rotarIzquierda(nodo);
    }
    return nodo;
  }

  // ── Insertar ────────────────────────────────────────────────
  void insertar(T dato) {
    raiz = _insertarRec(raiz, dato);
  }

  NodoAVL<T> _insertarRec(NodoAVL<T>? nodo, T dato) {
    if (nodo == null) return NodoAVL(dato);
    final cmp = dato.compareTo(nodo.dato);
    if (cmp < 0) {
      nodo.izquierdo = _insertarRec(nodo.izquierdo, dato);
    } else if (cmp > 0) {
      nodo.derecho = _insertarRec(nodo.derecho, dato);
    } else {
      return nodo; // no duplicados
    }
    return _balancear(nodo);
  }

  // ── Inorder ─────────────────────────────────────────────────
  List<T> inorder() {
    final res = <T>[];
    void rec(NodoAVL<T>? n) {
      if (n == null) return;
      rec(n.izquierdo);
      res.add(n.dato);
      rec(n.derecho);
    }
    rec(raiz);
    return res;
  }

  int get altura => _altura(raiz);
}
```

## Ejemplo de uso

```dart
void main() {
  final avl = ArbolAVL<int>();

  // Insertar en orden ascendente — en BST normal sería degenerado
  for (final v in [10, 20, 30, 40, 50, 25]) {
    avl.insertar(v);
  }

  print('Inorder: ${avl.inorder()}'); // [10, 20, 25, 30, 40, 50]
  print('Altura:  ${avl.altura}');    // 3 (balanceado, no 6)
}
```

## Los 4 casos de rotación

```
II  (fb>1, hijo izq fb>=0): rotación derecha simple
    z           y
   /           / \
  y     →     x   z
 /
x

DD  (fb<-1, hijo der fb<=0): rotación izquierda simple
  z               y
   \             / \
    y     →     z   x
     \
      x

ID  (fb>1, hijo izq fb<0): doble rotación izq-der
    z           z             x
   /           /             / \
  y     →     x     →       y   z
   \         /
    x       y

DI  (fb<-1, hijo der fb>0): doble rotación der-izq
  z           z               x
   \           \             / \
    y    →      x     →     z   y
   /             \
  x               y
```

## Tags

`dart` `estructuras-datos` `avl` `arbol-balanceado` `rotaciones` `flutter`
