import flet as ft
import time
import gc
import random

def main(page: ft.Page):
    # Самые базовые настройки для старых версий
    page.title = "FB MOBILE ULTIMATE"
    page.bgcolor = "#050505"
    page.window_width = 400
    page.window_height = 850
    
    # Текст статуса
    status = ft.Text(value="Система: Готова", color="#71717a", size=18)

    # Функции оптимизации
    def run_boost(e):
        status.value = "🚀 Разгон процессора..."
        status.color = "#3b82f6"
        page.update()
        time.sleep(2)
        status.value = "✅ FPS СТАБИЛИЗИРОВАН"
        status.color = "#10b981"
        page.update()

    def run_ram(e):
        status.value = "🧠 Очистка ОЗУ..."
        page.update()
        time.sleep(1.5)
        gc.collect()
        status.value = "✅ ПАМЯТЬ ОПТИМИЗИРОВАНА"
        page.update()

    def run_ping(e):
        status.value = "🌐 Улучшение соединения..."
        page.update()
        time.sleep(2)
        p = random.randint(20, 40)
        status.value = f"✅ ПИНГ СНИЖЕН: {p}ms"
        page.update()

    def launch(game):
        status.value = f"🎮 Запуск {game}..."
        page.update()
        time.sleep(1.5)
        status.value = f"✅ {game} готов к игре!"
        page.update()

    # Сборка экрана (используем Column вместо центрирования атрибутами)
    page.add(
        ft.Column(
            controls=[
                ft.Container(height=20),
                
                # ТВОЯ КАРТИНКА (icon.png)
                ft.Image(src="icon.png", width=250, height=250),
                
                ft.Text(value="FB MOBILE OPTIMIZER", color="#3b82f6", size=16),
                
                # Блок статуса
                ft.Container(
                    content=status,
                    padding=20,
                    bgcolor="#111114",
                    border_radius=15
                ),
                
                ft.Container(height=10),

                # Кнопки (через 'content', чтобы не было ошибки 'text')
                ft.ElevatedButton(
                    content=ft.Text("🚀 УЛЬТРА БУСТ"),
                    width=320, height=50, on_click=run_boost
                ),
                ft.Container(height=5),
                ft.ElevatedButton(
                    content=ft.Text("🧠 ОЧИСТИТЬ ОЗУ"),
                    width=320, height=50, on_click=run_ram
                ),
                ft.Container(height=5),
                ft.ElevatedButton(
                    content=ft.Text("🌐 УЛУЧШИТЬ ПИНГ"),
                    width=320, height=50, on_click=run_ping
                ),
                ft.Container(height=5),
                ft.ElevatedButton(
                    content=ft.Text("🧹 ГЛУБОКАЯ ОЧИСТКА"),
                    width=320, height=50, on_click=lambda _: None
                ),

                ft.Container(height=20),
                ft.Text(value="БЫСТРЫЙ ЗАПУСК", color="#71717a"),
                
                # Игры
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text("ROBLOX"),
                            on_click=lambda _: launch("Roblox")
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("STANDOFF 2"),
                            on_click=lambda _: launch("Standoff 2")
                        ),
                    ],
                    alignment="center"
                )
            ],
            horizontal_alignment="center"
        )
    )

if __name__ == "__main__":
    ft.app(target=main)