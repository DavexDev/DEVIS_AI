# Flutter — Widgets Comunes

## Ejecutar en Web

```bash
flutter run -d chrome       # desarrollo
flutter build web           # producción → build/web/
```

> Todos los widgets de esta referencia funcionan en Flutter Web sin modificaciones.

## Descripción

Referencia rápida de los widgets más usados en Flutter.

## Scaffold + AppBar + FloatingActionButton

```dart
Scaffold(
  appBar: AppBar(title: const Text('DEVIS')),
  body: const Center(child: Text('Hola DEVIS')),
  floatingActionButton: FloatingActionButton(
    onPressed: () {},
    child: const Icon(Icons.add),
  ),
);
```

## ListView + Card

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => Card(
    child: ListTile(
      leading: const Icon(Icons.math),
      title: Text(items[index]['titulo']!),
      subtitle: Text(items[index]['desc']!),
      trailing: const Icon(Icons.chevron_right),
      onTap: () {},
    ),
  ),
);
```

## AlertDialog

```dart
showDialog(
  context: context,
  builder: (_) => AlertDialog(
    title: const Text('DEVIS'),
    content: const Text('¿Confirmar operación?'),
    actions: [
      TextButton(onPressed: () => Navigator.pop(context), child: const Text('Cancelar')),
      ElevatedButton(onPressed: () {}, child: const Text('Aceptar')),
    ],
  ),
);
```

## BottomNavigationBar

```dart
BottomNavigationBar(
  currentIndex: _selectedIndex,
  onTap: (i) => setState(() => _selectedIndex = i),
  items: const [
    BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Inicio'),
    BottomNavigationBarItem(icon: Icon(Icons.calculate), label: 'Matemáticas'),
    BottomNavigationBarItem(icon: Icon(Icons.code), label: 'Código'),
  ],
);
```
