# Flutter — Lista de Notas / Registros

## Descripción

App con `TextField` para ingresar registros, lista dinámica con `ListView.builder`,
y confirmación de borrado con `AlertDialog`. Usa `StatefulWidget`, `TextEditingController` y `FilledButton`.

## Código completo

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const WidgetNotesApp());
}

class WidgetNotesApp extends StatelessWidget {
  const WidgetNotesApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Widget Notes',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF1F3A5F),
          brightness: Brightness.light,
        ),
        scaffoldBackgroundColor: const Color(0xFFF7F9FC),
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController controller = TextEditingController();
  final List<String> notes = [];

  // Agregar nota si el campo no está vacío
  void addNote() {
    if (controller.text.isNotEmpty) {
      setState(() {
        notes.add(controller.text);
        controller.clear();   // limpia el campo tras guardar
      });
    }
  }

  // Confirmar borrado con AlertDialog
  void deleteNote(int index) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Eliminar registro'),
        content: const Text('¿Deseas eliminar este registro?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),   // cancelar
            child: const Text('Cancelar'),
          ),
          FilledButton(
            onPressed: () {
              setState(() => notes.removeAt(index));
              Navigator.pop(context);                  // cerrar diálogo
            },
            child: const Text('Eliminar'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Registro de sistema'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // Campo de texto
            TextField(
              controller: controller,
              decoration: const InputDecoration(
                labelText: 'Registro rápido',
                hintText: 'Ej: Revisar estado del dashboard',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 12),

            // Botón guardar
            FilledButton(
              onPressed: addNote,
              child: const Text('Guardar registro'),
            ),

            const SizedBox(height: 20),

            // Lista dinámica o mensaje vacío
            Expanded(
              child: notes.isEmpty
                  ? const Center(
                      child: Text(
                        'Sin registros aún',
                        style: TextStyle(color: Colors.grey),
                      ),
                    )
                  : ListView.builder(
                      itemCount: notes.length,
                      itemBuilder: (context, index) {
                        return Card(
                          elevation: 1,
                          margin: const EdgeInsets.symmetric(vertical: 6),
                          child: ListTile(
                            title: Text(notes[index]),
                            subtitle: const Text('Registro manual'),
                            onTap: () => deleteNote(index),  // tap para borrar
                          ),
                        );
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }
}
```

## Conceptos clave

### TextEditingController

```dart
final TextEditingController controller = TextEditingController();

controller.text     // leer valor actual
controller.clear()  // vaciar el campo
```

### ListView.builder (lista dinámica)

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return ListTile(title: Text(items[index]));
  },
)
```

### AlertDialog con acciones

```dart
showDialog(
  context: context,
  builder: (context) => AlertDialog(
    title: const Text('Título'),
    content: const Text('Mensaje'),
    actions: [
      TextButton(onPressed: () => Navigator.pop(context), child: const Text('Cancelar')),
      FilledButton(onPressed: () { /* acción */ Navigator.pop(context); }, child: const Text('OK')),
    ],
  ),
);
```

### FilledButton vs TextButton vs ElevatedButton

| Widget           | Apariencia             | Uso                |
| ---------------- | ---------------------- | ------------------ |
| `FilledButton`   | Sólido, color primario | Acción principal   |
| `ElevatedButton` | Con sombra             | Acción importante  |
| `TextButton`     | Sin relleno            | Acción secundaria  |
| `OutlinedButton` | Con borde              | Acción alternativa |

## Tags

`flutter` `listview` `textfield` `alertdialog` `statefulwidget` `filledbutton` `controller`
