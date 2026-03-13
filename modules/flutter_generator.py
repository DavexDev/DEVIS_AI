"""
modules/flutter_generator.py
Generador de código Flutter a partir de descripciones en lenguaje natural.
Activo en v0.5.

Estrategia:
  1. Busca palabras clave en la descripción del usuario.
  2. Selecciona la plantilla más adecuada (o la genérica si no hay coincidencia).
  3. Si TinyLlama/Ollama está disponible, lo usa para personalizar el código
     tomando la plantilla como contexto base.
"""

# ──────────────────────────────────────────────────────────────────────────────
# Plantillas de código Flutter
# ──────────────────────────────────────────────────────────────────────────────

# Cada entrada: ( [palabras_clave], nombre_plantilla, código )
_TEMPLATES: list[tuple[list[str], str, str]] = [

    # ── Login / Autenticación ─────────────────────────────────────────────────
    (
        ["login", "autenticaci", "usuario", "contraseña", "password",
         "formulario", "iniciar sesion", "sign in"],
        "Pantalla de Login",
        '''\
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login',
      debugShowCheckedModeBanner: false,
      home: const LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey   = GlobalKey<FormState>();
  final _userCtrl  = TextEditingController();
  final _passCtrl  = TextEditingController();

  void _submit() {
    if (_formKey.currentState!.validate()) {
      // TODO: lógica de autenticación
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Iniciando sesión...')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Iniciar Sesión')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextFormField(
                controller: _userCtrl,
                decoration: const InputDecoration(labelText: 'Usuario'),
                validator: (v) => v!.isEmpty ? 'Campo requerido' : null,
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _passCtrl,
                decoration: const InputDecoration(labelText: 'Contraseña'),
                obscureText: true,
                validator: (v) => v!.length < 6 ? 'Mínimo 6 caracteres' : null,
              ),
              const SizedBox(height: 24),
              FilledButton(
                onPressed: _submit,
                child: const Text('Entrar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}''',
    ),

    # ── Lista / Notas / Items ─────────────────────────────────────────────────
    (
        ["lista", "notas", "item", "registro", "listview", "agregar",
         "eliminar", "crud"],
        "Lista de Items",
        '''\
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lista',
      debugShowCheckedModeBanner: false,
      home: const ListaPage(),
    );
  }
}

class ListaPage extends StatefulWidget {
  const ListaPage({super.key});

  @override
  State<ListaPage> createState() => _ListaPageState();
}

class _ListaPageState extends State<ListaPage> {
  final List<String> _items = [];
  final _ctrl = TextEditingController();

  void _agregar() {
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: const Text('Nuevo item'),
        content: TextField(
          controller: _ctrl,
          autofocus: true,
          decoration: const InputDecoration(hintText: 'Escribe algo...'),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Cancelar'),
          ),
          FilledButton(
            onPressed: () {
              if (_ctrl.text.isNotEmpty) {
                setState(() => _items.add(_ctrl.text.trim()));
                _ctrl.clear();
              }
              Navigator.pop(context);
            },
            child: const Text('Agregar'),
          ),
        ],
      ),
    );
  }

  void _eliminar(int index) {
    setState(() => _items.removeAt(index));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi Lista')),
      body: _items.isEmpty
          ? const Center(child: Text('No hay items. Toca + para agregar.'))
          : ListView.builder(
              itemCount: _items.length,
              itemBuilder: (ctx, i) => ListTile(
                title: Text(_items[i]),
                trailing: IconButton(
                  icon: const Icon(Icons.delete_outline),
                  onPressed: () => _eliminar(i),
                ),
              ),
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _agregar,
        child: const Icon(Icons.add),
      ),
    );
  }
}''',
    ),

    # ── Contador ──────────────────────────────────────────────────────────────
    (
        ["contador", "contar", "incrementar", "decrementar", "sumar",
         "stateful", "boton"],
        "Contador con StatefulWidget",
        '''\
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Contador',
      debugShowCheckedModeBanner: false,
      home: const ContadorPage(),
    );
  }
}

class ContadorPage extends StatefulWidget {
  const ContadorPage({super.key});

  @override
  State<ContadorPage> createState() => _ContadorPageState();
}

class _ContadorPageState extends State<ContadorPage> {
  int _count = 0;

  void _incrementar() => setState(() => _count++);
  void _decrementar() => setState(() => _count--);
  void _resetear()    => setState(() => _count = 0);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Contador'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            tooltip: 'Resetear',
            onPressed: _resetear,
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              '$_count',
              style: Theme.of(context).textTheme.displayLarge,
            ),
            const SizedBox(height: 24),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                FilledButton.tonal(
                  onPressed: _decrementar,
                  child: const Icon(Icons.remove),
                ),
                const SizedBox(width: 16),
                FilledButton(
                  onPressed: _incrementar,
                  child: const Icon(Icons.add),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}''',
    ),

    # ── Navegación / Rutas ────────────────────────────────────────────────────
    (
        ["navega", "ruta", "pagina", "pantalla", "go_router", "router",
         "push", "pop", "back"],
        "Navegación con go_router",
        '''\
// pubspec.yaml — agregar dependencia:
//   go_router: ^14.0.0

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

// ── Configuración del router ──────────────────────────────────────────────────
final _router = GoRouter(
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const HomePage(),
    ),
    GoRoute(
      path: '/detalle/:id',
      builder: (context, state) {
        final id = state.pathParameters['id']!;
        return DetallePage(id: id);
      },
    ),
  ],
);

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Navegación',
      debugShowCheckedModeBanner: false,
      routerConfig: _router,
    );
  }
}

// ── Página principal ──────────────────────────────────────────────────────────
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: Center(
        child: FilledButton(
          onPressed: () => context.go('/detalle/42'),
          child: const Text('Ver detalle'),
        ),
      ),
    );
  }
}

// ── Página de detalle ─────────────────────────────────────────────────────────
class DetallePage extends StatelessWidget {
  final String id;
  const DetallePage({super.key, required this.id});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Detalle #$id')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('Item: $id', style: const TextStyle(fontSize: 24)),
            const SizedBox(height: 16),
            OutlinedButton(
              onPressed: () => context.go('/'),
              child: const Text('Volver'),
            ),
          ],
        ),
      ),
    );
  }
}''',
    ),

    # ── Estado / Provider ─────────────────────────────────────────────────────
    (
        ["estado", "provider", "riverpod", "state", "setstate",
         "changenotifier", "notifier"],
        "Manejo de Estado con Provider",
        '''\
// pubspec.yaml — agregar dependencia:
//   provider: ^6.0.0

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// ── Modelo de estado ──────────────────────────────────────────────────────────
class AppState extends ChangeNotifier {
  int _valor = 0;
  int get valor => _valor;

  void incrementar() {
    _valor++;
    notifyListeners(); // notifica a todos los widgets que escuchan
  }

  void resetear() {
    _valor = 0;
    notifyListeners();
  }
}

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => AppState(),
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Estado con Provider',
      debugShowCheckedModeBanner: false,
      home: const EstadoPage(),
    );
  }
}

class EstadoPage extends StatelessWidget {
  const EstadoPage({super.key});

  @override
  Widget build(BuildContext context) {
    // watch() → reconstruye cuando cambia AppState
    final estado = context.watch<AppState>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Provider'),
        actions: [
          // read() → accede sin escuchar (no reconstruye)
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () => context.read<AppState>().resetear(),
          ),
        ],
      ),
      body: Center(
        child: Text(
          '${estado.valor}',
          style: const TextStyle(fontSize: 72),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => context.read<AppState>().incrementar(),
        child: const Icon(Icons.add),
      ),
    );
  }
}''',
    ),

    # ── Widget personalizado / Componente ─────────────────────────────────────
    (
        ["widget", "componente", "personalizado", "custom", "reutilizable",
         "stateless", "parametro"],
        "Widget Personalizado (StatelessWidget)",
        '''\
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Widget Personalizado',
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(title: const Text('Componentes')),
        body: const Padding(
          padding: EdgeInsets.all(16),
          child: Column(
            children: [
              // Reutilizamos el mismo widget con distintos parámetros
              TarjetaInfo(titulo: 'Flutter', descripcion: 'Framework UI'),
              SizedBox(height: 12),
              TarjetaInfo(titulo: 'Dart',    descripcion: 'Lenguaje de programación'),
              SizedBox(height: 12),
              TarjetaInfo(
                titulo: 'Personalizado',
                descripcion: 'Widget con parámetros opcionales',
                color: Colors.teal,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// ── Widget reutilizable ───────────────────────────────────────────────────────
class TarjetaInfo extends StatelessWidget {
  final String titulo;
  final String descripcion;
  final Color color;

  const TarjetaInfo({
    super.key,
    required this.titulo,
    required this.descripcion,
    this.color = Colors.deepPurple, // parámetro opcional con valor por defecto
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: color,
          child: Text(
            titulo[0],
            style: const TextStyle(color: Colors.white),
          ),
        ),
        title: Text(titulo),
        subtitle: Text(descripcion),
      ),
    );
  }
}''',
    ),
]

# Plantilla genérica (fallback)
_TEMPLATE_GENERIC = (
    "Página básica (Scaffold + AppBar)",
    '''\
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MiPagina(),
    );
  }
}

class MiPagina extends StatelessWidget {
  const MiPagina({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi Página')),
      body: const Center(
        child: Text(
          '¡Hola, Flutter!',
          style: TextStyle(fontSize: 24),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.touch_app),
      ),
    );
  }
}''',
)


# ──────────────────────────────────────────────────────────────────────────────
# Generador
# ──────────────────────────────────────────────────────────────────────────────

class FlutterGenerator:
    """
    Genera código Flutter/Dart a partir de una descripción en lenguaje natural.

    Flujo:
      1. Normaliza la descripción a minúsculas.
      2. Busca coincidencias de palabras clave en _TEMPLATES.
      3. Si hay coincidencia, devuelve esa plantilla.
      4. Si no hay coincidencia, devuelve la plantilla genérica.

    Si TinyLlama/Ollama está disponible (pasado como dependencia),
    la descripción se envía al modelo con la plantilla como contexto
    para obtener una respuesta más personalizada.
    """

    def __init__(self, ai_connector=None):
        """
        Args:
            ai_connector: instancia de OllamaConnector (opcional).
                          Si se omite, solo se usan las plantillas.
        """
        self._ai = ai_connector

    def generate(self, description: str) -> str:
        """
        Genera código Flutter para la descripción dada.

        Args:
            description: Texto en lenguaje natural, ej. 'pantalla de login con validación'.

        Returns:
            Código Dart/Flutter listo para usar, con encabezado explicativo.
        """
        if not description.strip():
            return "  Describe la pantalla o componente que necesitas generar."

        desc_lower = description.lower()

        # Buscar plantilla por palabras clave (primera coincidencia)
        nombre, codigo = self._match_template(desc_lower)

        # Si Ollama está disponible, usar IA para personalizar
        if self._ai and getattr(self._ai, "available", False):
            return self._generate_with_ai(description, nombre, codigo)

        return self._format_output(description, nombre, codigo)

    # ── Privados ───────────────────────────────────────────────────────────────

    def _match_template(self, desc_lower: str) -> tuple[str, str]:
        """Devuelve (nombre, código) de la primera plantilla que coincide."""
        for keywords, nombre, codigo in _TEMPLATES:
            if any(kw in desc_lower for kw in keywords):
                return nombre, codigo
        return _TEMPLATE_GENERIC  # fallback

    def _generate_with_ai(self, description: str, nombre: str, codigo: str) -> str:
        """Usa TinyLlama para personalizar la plantilla base."""
        prompt = (
            f"You are a Flutter expert. The user needs: '{description}'.\n"
            f"Below is a base template called '{nombre}'.\n"
            f"Adapt it to match the user's description. Return only Dart code.\n\n"
            f"```dart\n{codigo}\n```"
        )
        ai_response = self._ai.query(prompt)
        header = (
            f"\n  ── Flutter Generator (IA) ──────────────────────────────\n"
            f"  Descripción : {description}\n"
            f"  Plantilla   : {nombre}\n"
            f"  ─────────────────────────────────────────────────────────\n\n"
        )
        return header + ai_response

    @staticmethod
    def _format_output(description: str, nombre: str, codigo: str) -> str:
        """Formatea la salida sin IA."""
        header = (
            f"\n  ── Flutter Generator ───────────────────────────────────\n"
            f"  Descripción : {description}\n"
            f"  Plantilla   : {nombre}\n"
            f"  ─────────────────────────────────────────────────────────\n\n"
        )
        footer = (
            "\n\n  ── Para correr en web ──────────────────────────────────\n"
            "  flutter run -d chrome\n"
        )
        return header + codigo + footer
