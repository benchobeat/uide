import tkinter as tk
from tkinter import ttk, messagebox, font
import random
import string
import pyperclip
from tkinter import Frame, Label, Button, StringVar, IntVar, Radiobutton, Text, Spinbox

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class GeneradorContraseñas:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Generador de Contraseñas Seguras")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#f5f7fa')
        
        # Configuración de estilos
        self.style = ttk.Style()
        
        # Fuentes personalizadas
        self.title_font = ('Segoe UI', 18, 'bold')
        self.label_font = ('Segoe UI', 10)
        self.button_font = ('Segoe UI', 10, 'bold')
        self.result_font = ('Consolas', 12)
        
        # Colores
        self.primary_color = '#4a6cf7'
        self.secondary_color = '#6c757d'
        self.success_color = '#28a745'
        self.bg_color = '#f5f7fa'
        self.card_bg = '#ffffff'
        self.text_color = '#2d3748'
        
        # Configurar estilos para los widgets
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, foreground=self.text_color, font=self.label_font)
        self.style.configure('TButton', font=self.button_font, padding=8)
        self.style.configure('TNotebook', background=self.bg_color)
        self.style.configure('TNotebook.Tab', font=self.button_font, padding=[15, 5])
        self.style.map('TButton',
                     foreground=[('pressed', 'white'), ('active', 'white')],
                     background=[('pressed', self.primary_color), ('active', '#3a5bd9')])
        
        # Configurar el estilo del spinbox
        self.style.configure('TSpinbox', arrowsize=12, arrowcolor=self.primary_color)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Marco principal con padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            title_frame, 
            text="🔒 Generador de Contraseñas", 
            font=self.title_font,
            foreground=self.primary_color
        )
        title_label.pack(anchor='center')
        
        # Tarjeta de configuración
        card = ttk.Frame(main_frame, style='Card.TFrame')
        card.pack(fill=tk.X, pady=5, ipadx=10, ipady=10)
        
        # Estilo para la tarjeta
        card_style = ttk.Style()
        card_style.configure('Card.TFrame', background=self.card_bg, relief='solid', borderwidth=1, border=1)
        
        # Controles para longitud de caracteres
        controls = [
            ("Minúsculas (a-z)", 10),
            ("Mayúsculas (A-Z)", 10),
            ("Números (0-9)", 5),
            ("Caracteres especiales (!@#$%^&*)", 5)
        ]
        
        self.controles = []
        for i, (text, default) in enumerate(controls):
            frame = ttk.Frame(card)
            frame.pack(fill=tk.X, pady=5)
            
            label = ttk.Label(frame, text=text, width=25, anchor='w')
            label.pack(side=tk.LEFT, padx=5)
            
            var = tk.IntVar(value=default)
            spin = ttk.Spinbox(
                frame, 
                from_=0, 
                to=50, 
                width=5,
                textvariable=var,
                font=self.label_font,
                justify='center'
            )
            spin.pack(side=tk.RIGHT, padx=5)
            
            self.controles.append((var, spin))
        
        # Sección de complejidad
        ttk.Label(
            card, 
            text="Nivel de complejidad:", 
            font=('Segoe UI', 10, 'bold'),
            foreground=self.text_color
        ).pack(anchor='w', pady=(15, 5))
        
        self.complejidad = tk.StringVar(value="media")
        complejidades = [
            ("Baja", "baja"), 
            ("Media", "media"), 
            ("Alta", "alta")
        ]
        
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill=tk.X, pady=5)
        
        for text, value in complejidades:
            rb = ttk.Radiobutton(
                btn_frame, 
                text=text, 
                value=value, 
                variable=self.complejidad,
                style='Toolbutton'
            )
            rb.pack(side=tk.LEFT, padx=5, ipadx=10, ipady=3)
        
        # Botón de generación
        btn_generar = ttk.Button(
            main_frame, 
            text="🔑 Generar Contraseña", 
            command=self.generar_contraseña,
            style='Accent.TButton'
        )
        btn_generar.pack(pady=20, ipadx=20, ipady=8)
        
        # Estilo para el botón de acción principal
        self.style.configure('Accent.TButton', 
                           font=('Segoe UI', 11, 'bold'),
                           background=self.primary_color, 
                           foreground='white')
        
        # Área de resultado
        result_frame = ttk.LabelFrame(
            main_frame, 
            text=" Tu Contraseña Generada ",
            padding=15,
            style='Card.TFrame'
        )
        result_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.resultado = Text(
            result_frame, 
            height=4, 
            width=50, 
            font=self.result_font,
            wrap=tk.WORD,
            bd=0,
            highlightthickness=0,
            padx=10,
            pady=10,
            bg='#f8f9fa',
            fg=self.text_color
        )
        self.resultado.pack(fill=tk.BOTH, expand=True)
        
        # Botón para copiar al portapapeles
        btn_copiar = ttk.Button(
            main_frame, 
            text="📋 Copiar Contraseña", 
            command=self.copiar_portapapeles,
            style='Success.TButton'
        )
        btn_copiar.pack(ipadx=15, ipady=5)
        
        # Estilo para el botón de éxito
        self.style.configure('Success.TButton', 
                           background=self.success_color, 
                           foreground='white')
        
        # Footer
        footer = ttk.Label(
            main_frame, 
            text="© 2025 Generador de Contraseñas Seguras",
            foreground=self.secondary_color,
            font=('Segoe UI', 8)
        )
        footer.pack(side=tk.BOTTOM, pady=(20, 0))
    
    def crear_control(self, parent, texto, fila, columna, valor_inicial):
        ttk.Label(parent, text=texto).grid(row=fila, column=columna, sticky='w', pady=5, padx=5)
        var = tk.IntVar(value=valor_inicial)
        spin = ttk.Spinbox(parent, from_=0, to=50, width=5, textvariable=var)
        spin.grid(row=fila, column=columna+1, sticky='w', pady=5, padx=5)
        # Guardar referencia a los controles
        if not hasattr(self, 'controles'):
            self.controles = []
        self.controles.append((var, spin))
        return var
    
    def generar_contraseña(self):
        try:
            # Obtener valores de los controles
            if not hasattr(self, 'controles') or len(self.controles) < 4:
                messagebox.showerror("Error", "No se pudieron cargar los controles")
                return
                
            min = self.controles[0][0].get()  # Minúsculas
            may = self.controles[1][0].get()  # Mayúsculas
            num = self.controles[2][0].get()  # Números
            esp = self.controles[3][0].get()  # Especiales
            
            # Generar cada tipo de caracter
            minusculas = ''.join(random.choice(string.ascii_lowercase) for _ in range(min))
            mayusculas = ''.join(random.choice(string.ascii_uppercase) for _ in range(may))
            numeros = ''.join(random.choice(string.digits) for _ in range(num))
            especiales = ''.join(random.choice('!@#$%^&*') for _ in range(esp))
            
            # Combinar y mezclar
            contraseña = list(minusculas + mayusculas + numeros + especiales)
            random.shuffle(contraseña)
            contraseña = ''.join(contraseña)
            
            # Aplicar nivel de complejidad
            if self.complejidad.get() == "alta":
                if len(contraseña) < 12:
                    contraseña += ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%^&*') 
                                      for _ in range(12 - len(contraseña)))
            
            # Mostrar resultado
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, contraseña)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def copiar_portapapeles(self):
        contraseña = self.resultado.get(1.0, tk.END).strip()
        if contraseña:
            pyperclip.copy(contraseña)
            
            # Mostrar notificación de éxito
            top = tk.Toplevel(self.root)
            top.overrideredirect(True)
            top.geometry("300x80+{}+{}".format(
                self.root.winfo_x() + (self.root.winfo_width() - 300) // 2,
                self.root.winfo_y() + (self.root.winfo_height() - 80) // 2
            ))
            
            # Estilo de la notificación
            top.configure(bg='#28a745')
            
            # Contenido de la notificación
            label = tk.Label(
                top, 
                text="✓ Contraseña copiada al portapapeles",
                fg='white',
                bg='#28a745',
                font=('Segoe UI', 10, 'bold'),
                pady=20
            )
            label.pack(fill=tk.BOTH, expand=True)
            
            # Cerrar automáticamente después de 2 segundos
            top.after(2000, top.destroy)
        else:
            messagebox.showwarning(
                "Sin contraseña", 
                "No hay ninguna contraseña generada para copiar.",
                icon='warning'
            )

if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        import os
        os.system('pip install pyperclip')
        import pyperclip
        
    root = tk.Tk()
    app = GeneradorContraseñas(root)
    root.mainloop()
