# Dart — Equilibrio de Árboles (Factor de Balance)

## Factor de balance

El **factor de balance** (FB) de un nodo es la diferencia entre la altura de su subárbol izquierdo y su subárbol derecho:

```
FB(nodo) = altura(izquierdo) - altura(derecho)
```

- `FB = 0` → nodo perfectamente balanceado
- `FB = 1` → subárbol izquierdo un nivel más alto
- `FB = -1` → subárbol derecho un nivel más alto
- `|FB| > 1` → **desbalanceado** (AVL no lo permite)

## Implementación

```dart
class Nodo<T> {
  T dato;
  Nodo<T>? izquierdo;
  Nodo<T>? derecho;
  Nodo(this.dato);
}

/// Altura del árbol (-1 para árbol vacío)
int altura(Nodo? nodo) {
  if (nodo == null) return -1;
  final altIzq = altura(nodo.izquierdo);
  final altDer = altura(nodo.derecho);
  return 1 + (altIzq > altDer ? altIzq : altDer);
}

/// Factor de balance de un nodo
int factorBalance(Nodo? nodo) {
  if (nodo == null) return 0;
  return altura(nodo.izquierdo) - altura(nodo.derecho);
}

/// Verifica si el árbol está balanceado en altura (AVL condition)
/// Un árbol está balanceado si para TODOS sus nodos |FB| <= 1
bool estaBalanceado(Nodo? nodo) {
  if (nodo == null) return true;
  final fb = factorBalance(nodo);
  if (fb.abs() > 1) return false;
  return estaBalanceado(nodo.izquierdo) && estaBalanceado(nodo.derecho);
}

/// Devuelve el factor de balance de cada nodo en inorder
List<Map<String, int>> reporteBalance(Nodo? nodo) {
  if (nodo == null) return [];
  return [
    ...reporteBalance(nodo.izquierdo),
    {'dato': nodo.dato as int, 'fb': factorBalance(nodo)},
    ...reporteBalance(nodo.derecho),
  ];
}
```

## Ejemplo de uso

```dart
void main() {
  // Árbol balanceado:
  //        50       FB=0
  //       /  \
  //      30   70    FB=0, FB=0
  //     / \
  //    20  40       FB=0, FB=0

  final balanceado = Nodo(50)
    ..izquierdo = (Nodo(30)
      ..izquierdo = Nodo(20)
      ..derecho = Nodo(40))
    ..derecho = Nodo(70);

  print('¿Balanceado? ${estaBalanceado(balanceado)}');   // true
  print('FB raíz:     ${factorBalance(balanceado)}');    // 1

  // Árbol desbalanceado:
  //   10       FB=3
  //  /
  // 5          FB=2
  // /
  //3           FB=1
  ///
  //1           FB=0

  final desbalanceado = Nodo(10)
    ..izquierdo = (Nodo(5)
      ..izquierdo = (Nodo(3)
        ..izquierdo = Nodo(1)));

  print('¿Balanceado? ${estaBalanceado(desbalanceado)}');  // false
  print('FB raíz:     ${factorBalance(desbalanceado)}');   // 3

  // Reporte completo
  print(reporteBalance(balanceado));
  // [{dato: 20, fb: 0}, {dato: 30, fb: 0}, {dato: 40, fb: 0},
  //  {dato: 50, fb: 1}, {dato: 70, fb: 0}]
}
```

## Relación con AVL

Un árbol AVL mantiene `|FB| <= 1` para **todos** los nodos mediante rotaciones automáticas al insertar o eliminar. Ver [arbol_avl.md](arbol_avl.md) para la implementación completa con rotaciones.

## Comparación BST vs AVL

| Caso                           | BST                  | AVL                   |
| ------------------------------ | -------------------- | --------------------- |
| Inserción ordenada [1,2,3,4,5] | Degenerado, altura=4 | Balanceado, altura=2  |
| Búsqueda peor caso             | O(n)                 | O(log n)              |
| Overhead de inserción          | O(log n) prom        | O(log n) + rotaciones |

## Tags

`dart` `estructuras-datos` `avl` `factor-balance` `equilibrio` `arbol` `flutter`
