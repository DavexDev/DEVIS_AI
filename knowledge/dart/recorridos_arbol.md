# Dart — Recorridos de Árbol

## Recorridos básicos (recursivos)

```dart
class Nodo<T> {
  T dato;
  Nodo<T>? izquierdo;
  Nodo<T>? derecho;
  Nodo(this.dato);
}

class RecorridosArbol<T> {
  // ── Inorder: Izquierdo → Raíz → Derecho ─────────────────────────
  // En un BST produce los valores en orden ascendente
  List<T> inorder(Nodo<T>? nodo) {
    if (nodo == null) return [];
    return [
      ...inorder(nodo.izquierdo),
      nodo.dato,
      ...inorder(nodo.derecho),
    ];
  }

  // ── Preorder: Raíz → Izquierdo → Derecho ────────────────────────
  // Útil para copiar o serializar el árbol
  List<T> preorder(Nodo<T>? nodo) {
    if (nodo == null) return [];
    return [
      nodo.dato,
      ...preorder(nodo.izquierdo),
      ...preorder(nodo.derecho),
    ];
  }

  // ── Postorder: Izquierdo → Derecho → Raíz ───────────────────────
  // Útil para eliminar el árbol o evaluar expresiones
  List<T> postorder(Nodo<T>? nodo) {
    if (nodo == null) return [];
    return [
      ...postorder(nodo.izquierdo),
      ...postorder(nodo.derecho),
      nodo.dato,
    ];
  }

  // ── Por niveles (BFS) con cola ───────────────────────────────────
  List<T> porNiveles(Nodo<T>? raiz) {
    if (raiz == null) return [];
    final resultado = <T>[];
    final cola = [raiz];
    while (cola.isNotEmpty) {
      final nodo = cola.removeAt(0);
      resultado.add(nodo.dato);
      if (nodo.izquierdo != null) cola.add(nodo.izquierdo!);
      if (nodo.derecho != null) cola.add(nodo.derecho!);
    }
    return resultado;
  }
}
```

## Versiones iterativas

```dart
// Inorder iterativo con pila
List<T> inorderIterativo(Nodo<T>? raiz) {
  final resultado = <T>[];
  final pila = <Nodo<T>>[];
  Nodo<T>? actual = raiz;

  while (actual != null || pila.isNotEmpty) {
    while (actual != null) {
      pila.add(actual);
      actual = actual.izquierdo;
    }
    actual = pila.removeLast();
    resultado.add(actual.dato);
    actual = actual.derecho;
  }
  return resultado;
}

// Preorder iterativo con pila
List<T> preorderIterativo(Nodo<T>? raiz) {
  if (raiz == null) return [];
  final resultado = <T>[];
  final pila = [raiz];

  while (pila.isNotEmpty) {
    final nodo = pila.removeLast();
    resultado.add(nodo.dato);
    if (nodo.derecho != null) pila.add(nodo.derecho!);
    if (nodo.izquierdo != null) pila.add(nodo.izquierdo!);
  }
  return resultado;
}
```

## Ejemplo de uso

```dart
void main() {
  //        50
  //       /  \
  //      30   70
  //     / \
  //    20  40

  final raiz = Nodo(50)
    ..izquierdo = (Nodo(30)
      ..izquierdo = Nodo(20)
      ..derecho = Nodo(40))
    ..derecho = Nodo(70);

  final r = RecorridosArbol<int>();

  print('Inorder:    ${r.inorder(raiz)}');    // [20, 30, 40, 50, 70]
  print('Preorder:   ${r.preorder(raiz)}');   // [50, 30, 20, 40, 70]
  print('Postorder:  ${r.postorder(raiz)}');  // [20, 40, 30, 70, 50]
  print('Por niveles:${r.porNiveles(raiz)}'); // [50, 30, 70, 20, 40]
}
```

## Resumen visual

```
Árbol:         Inorder    Preorder   Postorder  Por niveles
    1          4,2,5,1,3  1,2,4,5,3  4,5,2,3,1  1,2,3,4,5
   / \
  2   3
 / \
4   5
```

## Tags

`dart` `estructuras-datos` `arbol` `recorrido` `inorder` `preorder` `postorder` `bfs` `flutter`
