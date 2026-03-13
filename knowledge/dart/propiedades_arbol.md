# Dart — Propiedades de Árboles Binarios

## Clase base

```dart
class Nodo<T> {
  T dato;
  Nodo<T>? izquierdo;
  Nodo<T>? derecho;
  Nodo(this.dato);
}
```

## Altura del árbol

```dart
/// Altura = número de aristas en el camino más largo desde la raíz a una hoja
/// Árbol vacío: -1  |  Árbol de un nodo: 0
int altura(Nodo? nodo) {
  if (nodo == null) return -1;
  final altIzq = altura(nodo.izquierdo);
  final altDer = altura(nodo.derecho);
  return 1 + (altIzq > altDer ? altIzq : altDer);
}
```

## Contar nodos

```dart
int contarNodos(Nodo? nodo) {
  if (nodo == null) return 0;
  return 1 + contarNodos(nodo.izquierdo) + contarNodos(nodo.derecho);
}

int contarHojas(Nodo? nodo) {
  if (nodo == null) return 0;
  if (nodo.izquierdo == null && nodo.derecho == null) return 1;
  return contarHojas(nodo.izquierdo) + contarHojas(nodo.derecho);
}
```

## Árbol degenerado

Un árbol es **degenerado** (o sesgado) si cada nodo tiene como máximo un hijo —
se comporta como una lista enlazada. Altura = n-1 con n nodos.

```dart
bool esDegenerado(Nodo? nodo) {
  if (nodo == null) return true;
  // Degenerado si ningún nodo tiene dos hijos
  if (nodo.izquierdo != null && nodo.derecho != null) return false;
  final hijo = nodo.izquierdo ?? nodo.derecho;
  return esDegenerado(hijo);
}
```

## Árbol lleno (Full Binary Tree)

Cada nodo tiene 0 o 2 hijos (nunca exactamente 1).

```dart
bool esLleno(Nodo? nodo) {
  if (nodo == null) return true;
  // Hoja: válido
  if (nodo.izquierdo == null && nodo.derecho == null) return true;
  // Si tiene exactamente un hijo: no es lleno
  if (nodo.izquierdo == null || nodo.derecho == null) return false;
  return esLleno(nodo.izquierdo) && esLleno(nodo.derecho);
}
```

## Árbol completo (Complete Binary Tree)

Todos los niveles llenos excepto posiblemente el último, que se llena de izq a der.

```dart
bool esCompleto(Nodo? raiz) {
  final total = contarNodos(raiz);
  return _esCompletoRec(raiz, 0, total);
}

bool _esCompletoRec(Nodo? nodo, int indice, int total) {
  if (nodo == null) return true;
  if (indice >= total) return false;
  return _esCompletoRec(nodo.izquierdo, 2 * indice + 1, total) &&
         _esCompletoRec(nodo.derecho,   2 * indice + 2, total);
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

  print('Altura:        ${altura(raiz)}');        // 2
  print('Nodos:         ${contarNodos(raiz)}');   // 5
  print('Hojas:         ${contarHojas(raiz)}');   // 3
  print('Degenerado:    ${esDegenerado(raiz)}');  // false
  print('Lleno:         ${esLleno(raiz)}');       // false (30 tiene 2 hijos, 70 tiene 0)
  print('Completo:      ${esCompleto(raiz)}');    // true

  // Árbol degenerado (lista):  1 → 2 → 3
  final deg = Nodo(1)..derecho = (Nodo(2)..derecho = Nodo(3));
  print('Degenerado2:  ${esDegenerado(deg)}');    // true
  print('Altura deg:   ${altura(deg)}');           // 2
}
```

## Resumen de tipos

| Tipo                | Definición                                   |
| ------------------- | -------------------------------------------- | ------------------------- | ---------------- |
| Lleno (Full)        | Todo nodo tiene 0 o 2 hijos                  |
| Completo (Complete) | Niveles completos, último nivel de izq a der |
| Perfecto (Perfect)  | Todos los niveles completamente llenos       |
| Degenerado          | Cada nodo tiene máximo 1 hijo                |
| Balanceado          |                                              | altura(izq) - altura(der) | ≤ 1 en todo nodo |

## Tags

`dart` `estructuras-datos` `arbol` `altura` `degenerado` `propiedades` `flutter`
