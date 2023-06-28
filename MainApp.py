from tkinter import *
from tkinter.ttk import Progressbar, Combobox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from eraser import dict_inflacion_31_12_2022, monto_conformato, many_points
import webbrowser
from datetime import datetime
from dateutil.relativedelta import relativedelta
from functools import partial

# outter functions & info


def show_loading_screen(parent):
    loading_window = Toplevel(parent)
    loading_window.title("Loading screen")
    loading_window.geometry("800x600+200+30")

    # Label and ProgressBar
    label = Label(loading_window, text="Cargando...", font=("Helvetica", 16))
    label.pack(pady=150)
    label = Progressbar(loading_window, mode="indeterminate", length=175)
    label.pack(pady=90)
    label.start()

    loading_window.update()
    return loading_window


def main_window_loaded(loading_window, calculator_main):
    loading_window.destroy()
    calculator_main.deiconify()


def show_loading_screen2(parent):
    loading_window2 = Toplevel(parent)
    loading_window2.title("Loading screen")
    loading_window2.geometry("500x575+200+30")

    # Label and ProgressBar
    label = Label(loading_window2, text="Cargando...", font=("Helvetica", 16))
    label.pack(pady=60)
    label = Progressbar(loading_window2, mode="indeterminate", length=175)
    label.pack(pady=80)
    label.start()

    loading_window2.update()
    return loading_window2


def main_window_loaded2(loading_window2, anticipos):
    loading_window2.destroy()
    anticipos.deiconify()


def block_typing(event):
    return "break"


def main_a():
    # inner function to close all windows if any is closed
    def close_all_windows():
        # Destroy all windows except the mainapp (main) window
        for window in windows:
            if window != mainapp:
                window.destroy()
        # Destroy the root (main) window
        mainapp.destroy()

    # initiate
    mainapp = Tk()
    windows = [mainapp]

    # resolution (size) & resizable
    mainapp.geometry('800x600+200+30')
    mainapp.resizable(False, False)

    # title
    mainapp.title('FC tools')

    # bg color
    mainapp.config(bg='gray')

    # logo/icon app

    mainapp.iconbitmap("img\\logo_ico.ico")

    # top panel(frame) & logo
    top_panel = Frame(mainapp, relief=RAISED, bd=1)
    top_panel.pack(side=TOP)

    logo = ImageTk.PhotoImage(Image.open("img\\logo.jpg"))
    label_logo = Label(top_panel, image=logo, bg='white', width=796, bd=3)
    label_logo.grid(row=0, column=0)

    titulo = Label(top_panel, text='Herramientas de trabajo / Working tools',
                   font=('Dosis', 18, 'bold'), bg='burlywood', width=53, bd=5)
    titulo.grid(row=1, column=0)

    # left panel

    left_panel = Frame(mainapp, relief=FLAT, bd=3, bg='light grey')
    left_panel.pack(side=LEFT, fill=BOTH, expand=True)

    # img's variables
    calculadora = ImageTk.PhotoImage(Image.open('img\\calculator.jpg'))
    dgii_icon = ImageTk.PhotoImage(Image.open('img\\espiralii-trnas2.png'))
    tss_icon = ImageTk.PhotoImage(Image.open('img\\tss.jpg'))
    config_icon = ImageTk.PhotoImage(Image.open('img\\config.png'))
    back_img = ImageTk.PhotoImage(Image.open('img\\boton_volver.png'))

    # main page windows

    def menu_calculator():
        mainapp.withdraw()

        # inner functions

        def volver_atras():
            calculator_main.withdraw()
            mainapp.deiconify()

        def validate_input(text):
            # Allow empty string as a valid input
            if not text:
                return True
            # Check if the entered text is a valid integer
            if text.isdigit():
                return True
            else:
                texto_resultado.delete(1.0, END)
                texto_resultado.insert(END, f"\n\n\t\t********** SOLO PUEDE UTILIZAR NUMEROS CON "
                                            f"DECIMALES **********")
                return False

        def on_entry_click1(event):
            if cuadro_ant1.get() == "Ingresos Totales":
                cuadro_ant1.delete(0, END)
                cuadro_ant1.configure(foreground="black")
                cuadro_ant1.configure(validate='key', validatecommand=(validate_cmd, '%P'))

        def on_entry_leave1(event):
            if cuadro_ant1.get() == '' or not cuadro_ant1.get().isdigit():
                cuadro_ant1.configure(validate='none')
                cuadro_ant1.insert(0, "Ingresos Totales")
                cuadro_ant1.configure(foreground="gray")

        def on_entry_click2(event):
            if cuadro_ant2.get() == "Impuesto Liquidado":
                cuadro_ant2.delete(0, END)
                cuadro_ant2.configure(foreground="black")
                cuadro_ant2.configure(validate='key', validatecommand=(validate_cmd, '%P'))

        def on_entry_leave2(event):
            if cuadro_ant2.get() == '' or not cuadro_ant2.get().isdigit():
                cuadro_ant2.configure(validate='none')
                cuadro_ant2.insert(0, "Impuesto Liquidado")
                cuadro_ant2.configure(foreground="gray")

        def on_entry_click3(event):
            if monthly_salary_entry.get() == "Salario mensual":
                monthly_salary_entry.delete(0, END)
                monthly_salary_entry.configure(foreground="black")
                monthly_salary_entry.configure(validate='key', validatecommand=(validate_cmd, '%P'))

        def on_entry_leave3(event):
            if monthly_salary_entry.get() == '' or not monthly_salary_entry.get().isdigit():
                monthly_salary_entry.configure(validate='none')
                monthly_salary_entry.insert(0, "Salario mensual")
                monthly_salary_entry.configure(foreground="gray")

        def on_entry_click4(event):
            if annual_salary_entry.get() == "Salario anual":
                annual_salary_entry.delete(0, END)
                annual_salary_entry.configure(foreground="black")
                annual_salary_entry.configure(validate='key', validatecommand=(validate_cmd, '%P'))

        def on_entry_leave4(event):
            if annual_salary_entry.get() == '' or not annual_salary_entry.get().isdigit():
                annual_salary_entry.configure(validate='none')
                annual_salary_entry.insert(0, "Salario anual")
                annual_salary_entry.configure(foreground="gray")

        def mensaje_cero():
            texto_resultado.delete(1.0, END)
            texto_resultado.insert(END, "\n\n\t\t\t***** DEBE INTRODUCIR UN VALOR MAYOR A CERO (0) *****")

        def cal_ret_tss():
            texto_resultado.delete(1.0, END)

            def texto_ret(ars, afp):
                texto_resultado.insert(END, f"Con el sueldo de RD$ "
                                            f"{monto_conformato.format(round(float(sueldo1.get()), 2))}\n\n")
                texto_resultado.insert(END, f"-Retención por Seguro de vejez, "
                                            f"discapacidad y sobrevivencia (pensiones): {many_points}"
                                            f"RD$ {monto_conformato.format(round(afp, 2))}\n")
                texto_resultado.insert(END, f"-Retención por Seguro familiar de salud: {many_points}"
                                            f"RD$ {monto_conformato.format(round(ars, 2))}\n\n"
                                            f"NOTA: Estos cálculos toman en cuenta los topes de SFS y pensiones.")

            if sueldo1.get() == 0:
                mensaje_cero()
            else:
                if float(sueldo1.get()) <= 187020:
                    ars = float(sueldo1.get()) * 0.0304
                    afp = float(sueldo1.get()) * 0.0287
                    texto_ret(ars, afp)

                elif 187020 <= float(sueldo1.get()) <= 374040:
                    ars = 187020 * 0.0304
                    afp = float(sueldo1.get()) * 0.0287
                    texto_ret(ars, afp)

                elif float(sueldo1.get()) >= 374040:
                    ars = 187020 * 0.0304
                    afp = 374040 * 0.0287
                    texto_ret(ars, afp)

        def cal_cont_tss():
            texto_resultado.delete(1.0, END)

            def texto_cont(ars, afp, srl1, srl2):
                texto_resultado.insert(END, f"Con el sueldo de RD$: "
                                            f"{monto_conformato.format(round(float(sueldo2.get()), 2))}\n")
                texto_resultado.insert(END, f"\n-Contribución por AFP(Fondo de Persiones): {many_points}RD$ "
                                            f"{monto_conformato.format(round(afp, 2))}\n")
                texto_resultado.insert(END, f"-Contribución por SFS(Seguro familiar de salud): {many_points}RD$ "
                                            f"{monto_conformato.format(round(ars, 2))}\n")
                texto_resultado.insert(END, f"-SRL (Seguro de Riesgo Laboral): ........Entre RD$ "
                                            f"{monto_conformato.format(round(srl1, 2))} "
                                            f"y RD${monto_conformato.format(round(srl2, 2))} "
                                            f"(Dependiendo el riesgo de la empresa)\n")
                texto_resultado.insert(END, f"-INFOTEP: {many_points}"
                                            f"RD${monto_conformato.format(round(sueldo2.get() * 0.01, 2))}")

            if sueldo2.get() == 0:
                mensaje_cero()
            else:
                if float(sueldo2.get()) <= 74808:
                    ars = float(sueldo2.get()) * 0.0709
                    afp = float(sueldo2.get()) * 0.071
                    srl1 = sueldo2.get() * 0.011
                    srl2 = sueldo2.get() * 0.013
                    texto_cont(ars, afp, srl1, srl2)

                elif 74808 <= float(sueldo2.get()) <= 187020:
                    ars = float(sueldo2.get()) * 0.0709
                    afp = float(sueldo2.get()) * 0.071
                    srl1 = 74808 * 0.011
                    srl2 = 74808 * 0.013
                    texto_cont(ars, afp, srl1, srl2)

                elif 187020 <= float(sueldo2.get()) <= 374040:
                    ars = 187020 * 0.0709
                    afp = float(sueldo2.get()) * 0.071
                    srl1 = 74808 * 0.011
                    srl2 = 74808 * 0.013
                    texto_cont(ars, afp, srl1, srl2)

                elif float(sueldo2.get()) >= 374040:
                    ars = 187020 * 0.0709
                    afp = 374040 * 0.071
                    srl1 = 74808 * 0.011
                    srl2 = 74808 * 0.013
                    texto_cont(ars, afp, srl1, srl2)

        def cal_isr_pf():

            texto_resultado.delete(1.0, END)

            if annual_salary_entry.get().isdigit() and monthly_salary_entry.get().isdigit():
                texto_resultado.insert(END, f"\n\n\t****** DEBE BORRAR UNO DE LOS DOS SALARIOS PARA PODER "
                                            f"HACER EL CALCULO ******")

            elif monthly_salary_entry.get().isdigit() and not annual_salary_entry.get().isdigit():
                x = float(monthly_salary_entry.get())
                if x <= 34685:
                    texto_resultado.insert(END, f"Con el sueldo colocado, se encuentra exento del pago de ISR.")
                elif 34685 <= x <= 52027.41:
                    y = x - 34685
                    texto_resultado.insert(END, f"Con el sueldo de: RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: RD$ {many_points}"
                                                f"{monto_conformato.format(round(y * 0.15, 2))}")
                elif 52027.41 <= float(monthly_salary_entry.get()) <= 72260.25:
                    y = x - 52027.41
                    texto_resultado.insert(END, f"Con el sueldo de RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((y * 0.20) + 2601.36, 2))}")
                elif 72260.25 <= float(monthly_salary_entry.get()):
                    y = x - 72260.25
                    texto_resultado.insert(END, f"Con el sueldo de: RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((y * 0.25) + 6647.93, 2))}")

            elif annual_salary_entry.get().isdigit() and not monthly_salary_entry.get().isdigit():
                x = float(annual_salary_entry.get())
                if x <= 416220.01:
                    texto_resultado.insert(END, f"Con el sueldo colocado, se encuentra exento del pago de ISR.")
                elif 416220.02 <= x <= 624329:
                    y = x - 416220.02
                    texto_resultado.insert(END, f"Con el sueldo de: RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: RD$ {many_points}"
                                                f"{monto_conformato.format(round(y * 0.15, 2))}")
                elif 624329 <= float(annual_salary_entry.get()) <= 867123:
                    y = x - 624329
                    texto_resultado.insert(END, f"Con el sueldo de RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((y * 0.20) + 31216, 2))}")
                elif 867123 <= float(annual_salary_entry.get()):
                    y = x - 867123
                    texto_resultado.insert(END, f"Con el sueldo de: RD$ "
                                                f"{monto_conformato.format(round(float(x), 2))}"
                                                f"\n\n")
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((y * 0.25) + 79776, 2))}")

            elif not annual_salary_entry.get().isdigit() and not monthly_salary_entry.get().isdigit():
                texto_resultado.insert(END, f"\n\n\t**** DEBE RELLENAR AL MENOS 1 DE LOS 2 SALARIOS PARA PODER"
                                            f" HACER EL CALCULO ****")

        def cal_rst_pf():
            texto_resultado.delete(1.0, END)
            if ingresos_rst_pf.get() == 0:
                mensaje_cero()
            else:
                remaining_income = round(0.6 * float(ingresos_rst_pf.get()), 2)
                texto_resultado.insert(END, f"NOTA 1: Esta calculadora solo toma en cuenta ingresos sujetos al "
                                            f"Régimen Tributario RST.\n")
                texto_resultado.insert(END, f"NOTA 2: El monto calculado no toma en cuenta las retenciones de ISR.\n")
                texto_resultado.insert(END, f"\nCon el ingreso anual de: RD$ "
                                            f"{monto_conformato.format(round(ingresos_rst_pf.get(), 2))}\n")
                if remaining_income <= 416220:
                    texto_resultado.insert(END, f"Con este ingreso se encuentra exento del pago de ISR.\n")
                elif 416220 <= remaining_income <= 624329:
                    x = remaining_income - 416220.02
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round(x * 0.15, 2))}\n")
                elif 624329 <= remaining_income <= 867123:
                    x2 = remaining_income - 624329
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((x2 * 0.20) + 31216, 2))}\n")
                elif 867123 <= remaining_income:
                    x3 = remaining_income - 867123
                    texto_resultado.insert(END, f"-La retención de ISR es de: {many_points}RD$ "
                                                f"{monto_conformato.format(round((x3 * 0.25) + 79776, 2))}\n")
                texto_resultado.insert(END, f"-Este monto a pagar se divide en 2 cuotas iguales.\n")

        def cal_rst_pj():
            texto_resultado.delete(1.0, END)
            if ingresos_rst_pj.get() == 0:
                mensaje_cero()
            else:
                isr_pj = round(float(ingresos_rst_pj.get()) * 0.07, 2)
                texto_resultado.insert(END, f"-El monto a pagar sería de: {many_points}RD$"
                                            f" {monto_conformato.format(isr_pj)}\n\n"
                                            f"-Dividido en 4 cuotas de: RD$ {monto_conformato.format(isr_pj / 4)}")

        def cal_vacas():
            texto_resultado.delete(1.0, END)
            if sueldo_vacay.get() == 0:
                mensaje_cero()
            else:
                sueldo_diario = round(float(sueldo_vacay.get()) / 23.83, 2)
                texto_resultado.insert(END, f"Con el sueldo de: RD$ "
                                            f"{monto_conformato.format(round(float(sueldo_vacay.get()), 2))}\n\n")
                texto_resultado.insert(END, f"-Si el empleado tiene entre 1 y 5 años en la empresa, le corresponden "
                                            f"{many_points}RD$ {monto_conformato.format(round(sueldo_diario * 14, 2))}\n")
                texto_resultado.insert(END, f"-Si el empleado tiene más de 5 años en la empresa, le corresponden "
                                            f"{many_points}RD$ {monto_conformato.format(round(sueldo_diario * 18, 2))}")

        def cal_ganancia_capital():
            texto_resultado.delete(1.0, END)
            if precio_venta.get() == 0 and precio_compra.get() == 0:
                texto_resultado.insert(END, "\n\n\t\t\t***** DEBE INTRODUCIR VALORES MAYORES A CERO (0) *****")
            elif precio_venta.get() == 0 or precio_compra.get() == 0:
                texto_resultado.insert(END, "\n\n\t\t***** DEBE INTRODUCIR VALORES MAYOR A CERO (0) EN AMBAS"
                                            " CASILLAS *****")
            else:
                ind_inf = dict_inflacion_31_12_2022.get(str(cuadro_fecha_impuesto.get_date().year))
                pc_ajustado = round(precio_compra.get(), 2) * ind_inf
                texto_resultado.insert(END, "-El indice de infación utilizado es el correspondiente a 2022-12.\n")
                texto_resultado.insert(END, "-Si el resultado es positivo = ganancia, si es negativo = pérdida.\n\n")
                texto_resultado.insert(END, f"-La ganancia de capital es de: {many_points}"
                                            f"RD$ "
                                            f"{monto_conformato.format(round(precio_venta.get() - pc_ajustado, 2))}")

        def recargos_interes():
            texto_resultado.delete(1.0, END)
            if cuadro_monto_recargos.get() == '':
                mensaje_cero()
            else:
                amount = float(cuadro_monto_recargos.get())
                delta = relativedelta(datetime.today().date(), cuadro_fecha_recargo.get_date())
                months_expired = (delta.years * 12 + delta.months) + 1
                percentage_surcharges = 0.1 + 0.04 * (months_expired - 1)
                percentage_interest = 0.011 * months_expired
                texto_resultado.insert(END, f"Con el monto de: RD$ {monto_conformato.format(amount)}\n\n"
                                            f"-Recargos: {many_points}"
                                            f"RD$ {monto_conformato.format(round(amount * percentage_surcharges, 2))}\n"
                                            f"-Intereses: {many_points}"
                                            f"RD$ {monto_conformato.format(round(amount * percentage_interest, 2))}")
                texto_resultado.insert(END, f'\n-Meses vencidos:  {months_expired}\nNOTA: Se utiliza la fecha de '
                                            f'hoy como fecha de pago.')

        def cal_ant():
            if cuadro_ant1.get().isdigit() and cuadro_ant2.get().isdigit():

                texto_resultado.delete(1.0, END)
                ant1 = round(float(cuadro_ant1.get()) * 0.015, 2)
                ant2 = round(float(cuadro_ant2.get()), 2)
                if ant1 > float(cuadro_ant2.get()):
                    texto_resultado.insert(END, f"En este caso se escoge el método de total de ingresos, "
                                                f"por ser el mayor.\n\n"
                                                f"-El monto total de anticipos anual sería de: {many_points}"
                                                f"RD$ {monto_conformato.format(ant1)}\n"
                                                f"-En cuotas mensuales sería de: {many_points}"
                                                f"RD$ {monto_conformato.format(round(ant1 / 12, 2))}")
                else:
                    texto_resultado.insert(END, f"En este caso se escoge el método del impuesto liquidado, "
                                                f"por ser el mayor.\n"
                                                f"\n-El monto total de anticipos anual sería de: {many_points}"
                                                f"RD$ {monto_conformato.format(ant2)}\n"
                                                f"-En cuotas mensuales sería de: {many_points}"
                                                f"RD$ {monto_conformato.format(round(ant2 / 12, 2))}")
                texto_resultado.insert(END,
                                       "\n\nNOTA: Este cálculo no toma en cuenta el saldo a favor de ISR, si tiene, "
                                       "debe rebajarlo para obtener lo real.")
            else:
                texto_resultado.delete(1.0, END)
                texto_resultado.insert(END, f"\n\n\t    ********** DEBE RELLENAR AMBAS CASILLAS CON"
                                            f" NUMEROS SIN DECIMALES **********")

        def cal_assets_cat1():
            texto_resultado.delete(1.0, END)
            year = fecha_prorrateo_cat1.get_date().year
            fecha1 = fecha_prorrateo_cat1.get_date()
            valor_contable = float(precio_cv_cat1.get())

            def texto_activos(total_days1, total_days2, daily_depreciation):
                texto_resultado.insert(END, f"Depreciación a prorratear (5%): RD$ "
                                            f"{monto_conformato.format(round((valor_contable * 0.05), 2))}\n\n"
                                            f"-La depreciación correspondiente para una VENTA ({total_days1} días) "
                                            f"sería de: {many_points}RD$ "
                                            f"{monto_conformato.format(round(daily_depreciation * total_days1, 2))}\n"
                                            f"-La depreciación correspondiente para una COMPRA ({total_days2} días) "
                                            f"sería de: {many_points}RD$ "
                                            f"{monto_conformato.format(round(daily_depreciation * total_days2, 2))}\n"
                                            f"\nNOTA: Este cálculo está hecho proporcionando los días del año "
                                            f"seleccionado.")

            if precio_cv_cat1.get() == 0:
                mensaje_cero()
            else:
                if menu_cierres.get() == 'Diciembre':
                    total_days1 = (fecha1 - datetime(year, 1, 1).date()).days + 1
                    total_days2 = (datetime(year, 12, 31).date() - fecha1).days
                    total_year_days = (datetime(year, 12, 31) - datetime(year, 1, 1)).days + 1
                    daily_depreciation = (valor_contable * 0.05) / total_year_days
                    texto_activos(total_days1, total_days2, daily_depreciation)
                elif menu_cierres.get() == 'Septiembre':
                    if fecha1.month >= 10:
                        total_days1 = (fecha1 - datetime(year, 10, 1).date()).days + 1
                        total_days2 = (datetime(year + 1, 9, 30).date() - fecha1).days
                        total_year_days = (datetime(year + 1, 9, 30) - datetime(year, 10, 1)).days + 1
                        daily_depreciation = (valor_contable * 0.05) / total_year_days
                        texto_activos(total_days1, total_days2, daily_depreciation)
                    else:
                        total_days1 = (fecha1 - datetime(year - 1, 10, 1).date()).days + 1
                        total_days2 = (datetime(year, 9, 30).date() - fecha1).days
                        total_year_days = (datetime(year, 9, 30) - datetime(year - 1, 10, 1)).days + 1
                        daily_depreciation = (valor_contable * 0.05) / total_year_days
                        print(total_days1, total_days2, total_year_days)
                        texto_activos(total_days1, total_days2, daily_depreciation)
                elif menu_cierres.get() == 'Junio':
                    if fecha1.month >= 7:
                        total_days1 = (fecha1 - datetime(year, 7, 1).date()).days + 1
                        total_days2 = (datetime(year + 1, 6, 30).date() - fecha1).days
                        total_year_days = (datetime(year + 1, 6, 30) - datetime(year, 7, 1)).days + 1
                        daily_depreciation = (valor_contable * 0.05) / total_year_days
                        texto_activos(total_days1, total_days2, daily_depreciation)
                    else:
                        total_days1 = (fecha1 - datetime(year - 1, 7, 1).date()).days + 1
                        total_days2 = (datetime(year, 6, 30).date() - fecha1).days
                        total_year_days = (datetime(year, 6, 30) - datetime(year - 1, 7, 1)).days + 1
                        daily_depreciation = (valor_contable * 0.05) / total_year_days
                        print(total_days1, total_days2, total_year_days)
                        texto_activos(total_days1, total_days2, daily_depreciation)
                elif menu_cierres.get() == 'Marzo':
                    if fecha1.month >= 4:
                        total_days1 = (fecha1 - datetime(year, 4, 1).date()).days + 1
                        total_days2 = (datetime(year + 1, 3, 31).date() - fecha1).days
                        total_year_days = (datetime(year + 1, 3, 31) - datetime(year, 4, 1)).days + 1
                        daily_depreciation = (valor_contable * 0.05) / total_year_days
                        texto_activos(total_days1, total_days2, daily_depreciation)
                    else:
                        total_days1 = (fecha1 - datetime(year - 1, 4, 1).date()).days + 1
                        total_days2 = (datetime(year, 3, 31).date() - fecha1).days
                        total_year_days = (datetime(year, 3, 31) - datetime(year - 1, 4, 1)).days + 1
                        daily_depreciation = (precio_cv_cat1.get() * 0.05) / total_year_days
                        print(total_days1, total_days2, total_year_days)
                        texto_activos(total_days1, total_days2, daily_depreciation)
                else:
                    texto_resultado.insert(END, "\n\n\t\t\t***** DEBE INTRODUCIR UN PERIODO DE CIERRE *****")

        # Top level window

        def recargos_intereses_ant():
            calculator_main.withdraw()

            # Inner functions

            def volver_atras3():
                anticipos.withdraw()
                calculator_main.deiconify()

            def on_entry_click(event, i):
                if entry_widgets[i].get() == "Anticipo " + str(i + 1):
                    entry_widgets[i].delete(0, END)
                    entry_widgets[i].configure(foreground="black")
                    entry_widgets[i].configure(validate='key', validatecommand=(validate_cmd, '%P'))

            def on_entry_leave(event, i):
                if entry_widgets[i].get() == '' or not entry_widgets[i].get().isdigit():
                    entry_widgets[i].configure(validate='none')
                    entry_widgets[i].insert(0, "Anticipo " + str(i + 1))
                    entry_widgets[i].configure(foreground="gray")

            def validate_input(text):
                # Allow empty string as a valid input
                if not text:
                    return True
                # Check if the entered text is a valid integer
                if text.isdigit():
                    return True
                else:
                    text_box.delete(1.0, END)
                    text_box.insert(END, f"\n\n\n\n\n\n***** SOLO PUEDE UTILIZAR NUMEROS SIN DECIMALES *****")
                    return False

            def calculate_ants():
                text_box.delete(1.0, END)
                fecha_pago = pay_date.get_date()
                total_surchages = 0
                total_interest = 0
                for i in range(12):
                    if entry_widgets[i].get().isdigit():
                        delta = relativedelta(fecha_pago, entry_date[i].get_date())
                        months_expired = (delta.years * 12 + delta.months) + 1
                        amount = float(entry_widgets[i].get())
                        percentage_surcharges = 0.1 + 0.04 * (months_expired - 1)
                        percentage_interest = 0.011 * months_expired
                        text_box.insert(END,
                                        f"Ant {i + 1}: Rec: "
                                        f"{monto_conformato.format(round(amount * percentage_surcharges, 2))}"
                                        f" Int: {monto_conformato.format(round(amount * percentage_interest, 2))}\n")
                        total_surchages += amount * percentage_surcharges
                        total_interest += amount * percentage_interest
                    else:
                        text_box.insert(END, f"Ant. {i + 1}: N/a\n")
                text_box.insert(END, f"\nTotal de Recargos: {monto_conformato.format(round(total_surchages, 2))}\n"
                                     f"Total de Intereses: {monto_conformato.format(round(total_interest, 2))}")

            # app & size

            anticipos = Toplevel(calculator_main)
            anticipos.withdraw()

            anticipos.geometry('500x575+200+30')
            anticipos.resizable(False, False)

            # closing all apps config

            anticipos.protocol("WM_DELETE_WINDOW", close_all_windows)
            windows.append(anticipos)

            # initial loading screen

            loading_window2 = show_loading_screen2(calculator_main)

            # title
            anticipos.title('Calculadora Recargos e Intereses de Anticipos')

            # bg color
            anticipos.config(bg='light grey')

            # icono/logo

            anticipos.iconbitmap("img\\logo_ico.ico")

            # validation number command

            validate_cmd = anticipos.register(validate_input)

            # Frames

            top_panel_ant = Frame(anticipos, relief=RAISED, bd=2, bg='burlywood')
            top_panel_ant.pack(side=TOP, fill=X, expand=True)

            top_panel_ant2 = Frame(anticipos, relief=RAISED, bd=2)
            top_panel_ant2.pack(side=TOP, fill=X, expand=True)

            top_panel_ant3 = Frame(anticipos, relief=RAISED, bd=2, bg='burlywood')
            top_panel_ant3.pack(side=TOP, fill=X, expand=True)
            top_panel_ant3.grid_columnconfigure(0, weight=1)

            # Frame 1 - Main Title & Sub-titles
            subtitles = ['Monto:', 'Fecha de Vencimiento:', '    Cuadro de Resultados:']

            ant_title = Label(top_panel_ant, text="   Recargos e Intereses - Anticipos",
                              font=('Times New Roman', 24, 'bold'), bg='burlywood',
                              bd=7)
            ant_title.grid(row=0, column=0, columnspan=4)

            for i in range(3):
                title = Label(top_panel_ant, text=subtitles[i],
                              font=('Times New Roman', 12), bg='burlywood', bd=3)
                title.grid(row=1, column=i)

            # Frame 2 - Column 0 - Widgets & placing code

            entry_widgets = []
            entry_date = []
            for i in range(12):
                entry = Entry(top_panel_ant2, font=('Times New Roman', 11),
                              width=12, bd=2, justify=CENTER, foreground="gray")
                entry.insert(0, "Anticipo " + str(i + 1))
                entry.grid(row=i, column=0)
                entry_widgets.append(entry)

            for i, entry_widget in enumerate(entry_widgets):
                entry_widget.bind("<FocusIn>", partial(on_entry_click, i=i))
                entry_widget.bind("<FocusOut>", partial(on_entry_leave, i=i))

            # Frame 2 - Column 1 - Widgets & placing code

            for i in range(12):
                entry = DateEntry(top_panel_ant2, font=('Times New Roman', 11),
                                  width=10, bd=2, justify=CENTER)
                entry.grid(row=i, column=2)
                entry_date.append(entry)

            # Frame 2 - spaces between all columns
            counters = 1
            while counters < 4:
                white_space = Label(top_panel_ant2, text=' ', bd=2, font=('Times New Roman', 12),
                                    width=1, height=16)
                white_space.grid(row=0, rowspan=12, column=counters)
                counters += 2

            # Frame 2 - Column 2 - Widgets & placing code
            text_box = Text(top_panel_ant2, height=21, width=30, font=('Dosis', 12))
            text_box.grid(row=0, column=4, rowspan=13)
            text_box.bind("<KeyPress>", block_typing)

            # Frame 2 - row 12 - Payment date

            pay_label = Label(top_panel_ant2, text='Fecha de pago:', font=('Times New Roman', 12))
            pay_date = DateEntry(top_panel_ant2, font=('Times New Roman', 11),
                                 width=10, bd=2, justify=CENTER)
            pay_label.grid(row=12, column=0, columnspan=1)
            pay_date.grid(row=12, column=2)

            # Frame 2 - row 13 - Calculate button
            submit_button = Button(top_panel_ant2, text="Calcular", command=calculate_ants)
            submit_button.grid(row=13, column=0, columnspan=3)

            # Frame 3 - text and back button

            texto_volver = Label(top_panel_ant3, text='Volver atrás:', font=('Times New Roman', 12, 'bold'),
                                 bg='burlywood')
            texto_volver.grid(row=0, column=0)

            boton_volver = Button(top_panel_ant3, image=back_img, bd=2, command=volver_atras3, bg="burlywood")
            boton_volver.grid(row=1, column=0)

            # avoid end app
            anticipos.after(800, lambda: main_window_loaded2(loading_window2, anticipos))

        # main
        calculator_main = Toplevel(mainapp)
        calculator_main.withdraw()

        # close all window config
        calculator_main.protocol("WM_DELETE_WINDOW", close_all_windows)
        windows.append(calculator_main)

        # loading screen & resolution
        loading_window = show_loading_screen(calculator_main)

        calculator_main.geometry('800x600+200+30')
        calculator_main.resizable(False, False)

        # title
        calculator_main.title('Calculadoras / Calculators')

        # bg color
        calculator_main.config(bg='light grey')

        # icono/logo

        calculator_main.iconbitmap("img\\logo_ico.ico")

        # validation number command

        validate_cmd = calculator_main.register(validate_input)

        # frames

        top_panel_cal = Frame(calculator_main, relief=RAISED, bd=1)
        top_panel_cal.pack(side=TOP)

        right_panel_cal = Frame(calculator_main, relief=RAISED, bd=1, bg='burlywood')
        right_panel_cal.pack(side=BOTTOM)

        left_panel_cal = Frame(calculator_main, relief=RAISED, bd=1, bg='burlywood')
        left_panel_cal.pack(side=TOP, fill=X, expand=True)

        button_frame = Frame(left_panel_cal, relief=RAISED, bd=3, bg='gray')
        button_frame.grid(row=10, rowspan=11, column=0)

        # main title

        cal_title = Label(top_panel_cal, text="Calculadoras / Calculators",
                          font=('Times New Roman', 32, 'bold'), bg='burlywood',
                          bd=7, width=600)
        cal_title.pack()

        # row 0 (lines between columns and rows)

        counters = 0

        # row 1 & 2 - Text & widget

        titulos_row1 = ['Retención\nTSS Empleados', 'Contribución\nTSS Empleador',
                        'Retención ISR\nEmpleados', 'RST Persona Física\n(por ingresos)',
                        'RST Empresas']
        titulos_row2 = ['Sueldo:', 'Sueldo:', 'Ingresos totales:', 'Ingresos totales:']

        monthly_salary_entry = Entry(left_panel_cal, font=('Times New Roman', 11),
                                     width=16, bd=2, justify=CENTER, foreground="gray")
        monthly_salary_entry.insert(0, "Salario mensual")
        monthly_salary_entry.bind("<FocusIn>", on_entry_click3)
        monthly_salary_entry.bind("<FocusOut>", on_entry_leave3)

        # row 1 placing code

        for empleado in titulos_row1:
            row_1 = Label(left_panel_cal, text=empleado, font=('Times New Roman', 12, 'bold'),
                          bg='burlywood', bd=2)
            row_1.grid(row=0, column=counters)
            counters += 2
        counters = 0

        # row 2 placing code

        monthly_salary_entry.grid(row=1, column=4)

        for texto in titulos_row2:
            if counters == 4:
                counters += 2
            row_2 = Label(left_panel_cal, text=texto, font=('Times New Roman', 12),
                          bg='burlywood', height=1, bd=2)
            row_2.grid(row=1, column=counters)
            counters += 2
        counters = 0

        # row 3 - widgets

        sueldo1 = IntVar()
        cuadro_sueldo1 = Entry(left_panel_cal, font=('Times New Roman', 11),
                               width=16, bd=2, textvariable=sueldo1, justify=CENTER,
                               validate='key', validatecommand=(validate_cmd, '%P'))
        sueldo2 = IntVar()
        cuadro_sueldo2 = Entry(left_panel_cal, font=('Times New Roman', 11),
                               width=16, bd=2, textvariable=sueldo2, justify=CENTER,
                               validate='key', validatecommand=(validate_cmd, '%P'))

        annual_salary_entry = Entry(left_panel_cal, font=('Times New Roman', 11),
                                    width=16, bd=2, justify=CENTER, fg="gray")
        annual_salary_entry.insert(0, "Salario anual")
        annual_salary_entry.bind("<FocusIn>", on_entry_click4)
        annual_salary_entry.bind("<FocusOut>", on_entry_leave4)

        ingresos_rst_pf = IntVar()
        cuadro_ing_rst = Entry(left_panel_cal, font=('Times New Roman', 11),
                               width=16, bd=2, textvariable=ingresos_rst_pf, justify=CENTER,
                               validate='key', validatecommand=(validate_cmd, '%P'))
        ingresos_rst_pj = IntVar()
        cuadro_ing_rst2 = Entry(left_panel_cal, font=('Times New Roman', 11),
                                width=16, bd=2, textvariable=ingresos_rst_pj, justify=CENTER,
                                validate='key', validatecommand=(validate_cmd, '%P'))

        # row 3 - Placing code

        entry_list = [cuadro_sueldo1, cuadro_sueldo2, annual_salary_entry, cuadro_ing_rst, cuadro_ing_rst2]

        for entrys in entry_list:
            entrys.grid(row=2, column=counters)
            counters += 2
        counters = 0

        # row 4 - Widgets

        calculate_ret_tss = Button(left_panel_cal, text='Calcular', bd=2,
                                   font=('Times New Roman', 11),
                                   command=cal_ret_tss)
        calculate_cont_tss = Button(left_panel_cal, text='Calcular', bd=2,
                                    font=('Times New Roman', 11),
                                    command=cal_cont_tss)
        calculate_ret_isr = Button(left_panel_cal, text='Calcular', bd=2,
                                   font=('Times New Roman', 11),
                                   command=cal_isr_pf)
        calculate_rst_pf = Button(left_panel_cal, text='Calcular', bd=2,
                                  font=('Times New Roman', 11),
                                  command=cal_rst_pf)
        calculate_rst_pj = Button(left_panel_cal, text='Calcular', bd=2,
                                  font=('Times New Roman', 11),
                                  command=cal_rst_pj)

        # row 4 - Placing code

        calculate_list = [calculate_ret_tss, calculate_cont_tss, calculate_ret_isr,
                          calculate_rst_pf, calculate_rst_pj]

        for calculate in calculate_list:
            calculate.grid(row=3, column=counters)
            counters += 2
        counters = 0

        # row 5 & 6 - text
        titulos_row5 = ['Vacaciones', 'Ganancia de Capital\n(Inmuebles - 31/12)',
                        'Recargos e Intereses\n(IT-1, IR-17, IR-3...)', 'Anticipos del\nISR',
                        'Prorrateo de De-\npreciación Cat. 1']
        titulos_row6 = ['Sueldo mensual:', 'Precio de Compra:', 'Monto:', 'F. Compra/Venta:']

        # row 5 Placing code

        for titulos in titulos_row5:
            row_5 = Label(left_panel_cal, text=titulos, font=('Times New Roman', 12, 'bold'),
                          bg='burlywood', bd=2)
            row_5.grid(row=4, column=counters)
            counters += 2
        counters = 0

        # row 6 - Placing code

        for titulos in titulos_row6:
            if counters == 6:
                counters += 2
            row_6 = Label(left_panel_cal, text=titulos, font=('Times New Roman', 12),
                          bg='burlywood', bd=2)
            row_6.grid(row=5, column=counters)
            counters += 2
        counters = 0

        # row 7 - Widgets

        sueldo_vacay = IntVar()
        cuadro_sueldo4 = Entry(left_panel_cal, font=('Times New Roman', 11),
                               width=16, bd=2, textvariable=sueldo_vacay, justify=CENTER,
                               validate='key', validatecommand=(validate_cmd, '%P'))
        precio_compra = IntVar()
        cuadro_precio_compra = Entry(left_panel_cal, font=('Times New Roman', 11),
                                     width=16, bd=2, textvariable=precio_compra, justify=CENTER,
                                     validate='key', validatecommand=(validate_cmd, '%P'))

        cuadro_monto_recargos = Entry(left_panel_cal, font=('Times New Roman', 11),
                                      width=16, bd=2, justify=CENTER,
                                      validate='key', validatecommand=(validate_cmd, '%P'))

        ant_button1 = Button(left_panel_cal, text='Calcular los \n Recargos e Intereses', bd=2,
                             font=('Times New Roman', 11), command=recargos_intereses_ant)
        ant_button1.grid(row=5, column=6, rowspan=2)

        fecha_prorrateo_cat1 = DateEntry(left_panel_cal, font=('Times New Roman', 11),
                                         width=15, bd=2, justify=CENTER)

        # row 7 - Placing code
        entry_list2 = [cuadro_sueldo4, cuadro_precio_compra, cuadro_monto_recargos, fecha_prorrateo_cat1]

        for entrys in entry_list2:
            if counters == 6:
                counters += 2
            entrys.grid(row=6, column=counters)
            counters += 2
        counters = 2

        # row 8 - Button

        calculate_vacas = Button(left_panel_cal, text='Calcular', bd=2,
                                 font=('Times New Roman', 11), command=cal_vacas)
        calculate_vacas.grid(row=7, column=0)

        # row 8 - Placing code
        list_row8 = ['Precio de Venta:', 'Fecha de Vencimiento:', 'Cuotas anticipos:', 'Valor Contable:']

        for titulos in list_row8:
            row_7 = Label(left_panel_cal, text=titulos, font=('Times New Roman', 12),
                          bg='burlywood', bd=2)
            row_7.grid(row=7, column=counters)
            counters += 2
        counters = 2

        # row 9 - Widgets

        precio_venta = IntVar()
        cuadro_precio_venta = Entry(left_panel_cal, font=('Times New Roman', 11),
                                    width=16, bd=2, textvariable=precio_venta, justify=CENTER,
                                    validate='key', validatecommand=(validate_cmd, '%P'))

        cuadro_fecha_recargo = DateEntry(left_panel_cal, font=('Times New Roman', 11),
                                         width=16, bd=2, justify=CENTER)

        cuadro_ant1 = Entry(left_panel_cal, font=('Times New Roman', 11),
                            width=17, bd=2, justify=CENTER, foreground="gray")
        cuadro_ant1.insert(0, "Ingresos Totales")
        cuadro_ant1.bind("<FocusIn>", on_entry_click1)
        cuadro_ant1.bind("<FocusOut>", on_entry_leave1)

        precio_cv_cat1 = IntVar()
        cuadro_pro_cat1 = Entry(left_panel_cal, font=('Times New Roman', 11),
                                width=16, bd=2, textvariable=precio_cv_cat1, justify=CENTER,
                                validate='key', validatecommand=(validate_cmd, '%P'))

        # row 9 - Placing code
        entry_list3 = [cuadro_precio_venta, cuadro_fecha_recargo, cuadro_ant1, cuadro_pro_cat1]

        for entrys in entry_list3:
            entrys.grid(row=8, column=counters)
            counters += 2
        counters = 2

        # row 10 - Widgets

        text = Label(left_panel_cal, text='Fecha de adquisición:', font=('Times New Roman', 12),
                     bg='burlywood', bd=2)

        calculate_recargos = Button(left_panel_cal, text='Calcular', bd=2,
                                    font=('Times New Roman', 11), command=recargos_interes)

        cuadro_ant2 = Entry(left_panel_cal, font=('Times New Roman', 11),
                            width=17, bd=2, justify=CENTER, foreground="gray")
        cuadro_ant2.insert(0, "Impuesto Liquidado")
        cuadro_ant2.bind("<FocusIn>", on_entry_click2)
        cuadro_ant2.bind("<FocusOut>", on_entry_leave2)

        tipo_cierre = Label(left_panel_cal, text='Período de Cierre:', font=('Times New Roman', 12),
                            bg='burlywood', bd=2)

        # row 10 - Placing code

        row10 = [text, calculate_recargos, cuadro_ant2, tipo_cierre]

        for items in row10:
            items.grid(row=9, column=counters)
            counters += 2
        counters = 1

        # row 11 - Widget & placing

        cuadro_fecha_impuesto = DateEntry(left_panel_cal, font=('Times New Roman', 11),
                                          width=16, bd=2, justify=CENTER)
        cuadro_fecha_impuesto.grid(row=10, column=2)

        cal_ant_button = Button(left_panel_cal, text='Calcular', bd=2,
                                font=('Times New Roman', 11),
                                command=cal_ant)
        cal_ant_button.grid(row=10, column=6)

        menu_cierres = Combobox(left_panel_cal, values=["Marzo", "Junio", "Septiembre", "Diciembre"],
                                width=14, justify=CENTER, font=('Times New Roman', 11))
        menu_cierres.grid(row=10, column=8)
        menu_cierres.bind("<KeyPress>", block_typing)

        # row 12 - Widget & placing

        calculate_ganancia_capital = Button(left_panel_cal, text='Calcular', bd=2,
                                            font=('Times New Roman', 11),
                                            command=cal_ganancia_capital)
        calculate_ganancia_capital.grid(row=11, column=2)

        button_cal_assets = Button(left_panel_cal, text='Calcular', bd=2,
                                   font=('Times New Roman', 11), command=cal_assets_cat1)
        button_cal_assets.grid(row=11, column=8)

        # separators between columns & rows

        while counters < 8:
            white_space = Label(left_panel_cal, text='  ', bd=2, font=('Times New Roman', 16),
                                bg='lightgray', width=2, height=16)
            white_space.grid(row=0, rowspan=12, column=counters)
            counters += 2

        # boton de volver de la row 9 a la 10

        texto_volver = Label(left_panel_cal, text='Volver atrás:', font=('Times New Roman', 12, 'bold'),
                             bg='burlywood')
        texto_volver.grid(row=9, column=0)

        boton_volver = Button(button_frame, image=back_img, bd=2, command=volver_atras)
        boton_volver.grid(row=10, rowspan=1, column=0)

        # title and results box (bottom frame) & block writing inside text

        resultado = Label(right_panel_cal, text='Resultados',
                          font=('Times New Roman', 12, 'bold'),
                          bg='burlywood', bd=2)
        resultado.grid(row=0, column=0)

        texto_resultado = Text(right_panel_cal,
                               font=('Dosis', 11, 'bold'),
                               bd=2,
                               width=99,
                               height=6)
        texto_resultado.grid(row=1, column=0)

        texto_resultado.bind("<KeyPress>", block_typing)

        calculator_main.after(300, lambda: main_window_loaded(loading_window, calculator_main))

    def menu_dgii():
        mainapp.withdraw()

        # functions

        def volver_atras2():
            dgii_main.withdraw()
            mainapp.deiconify()

        def consult_1():
            webbrowser.open('https://dgii.gov.do/herramientas/consultas/Paginas/RNC.aspx')

        def consult_2():
            webbrowser.open('https://dgii.gov.do/herramientas/consultas/Paginas/NCF-.aspx')

        def consult_forms():
            webbrowser.open('https://dgii.gov.do/herramientas/formularios/Paginas/default.aspx')

        # main
        dgii_main = Toplevel(mainapp)

        # resolution
        dgii_main.geometry('600x400+200+30')
        dgii_main.resizable(False, False)

        # title
        dgii_main.title('Herramientas de DGII (Dirección General de Impuestos Internos)')

        # Closing all apps config

        dgii_main.protocol("WM_DELETE_WINDOW", close_all_windows)
        windows.append(dgii_main)

        # bg color
        dgii_main.config(bg='light grey')

        # icono/logo

        dgii_main.iconbitmap("img\\logo_ico.ico")

        # top panel & title
        top_panel_dgii = Frame(dgii_main, relief=RAISED, bd=1)
        top_panel_dgii.pack(side=TOP)

        titulo_dgii = Label(top_panel_dgii, text='Herramientas DGII',
                            font=('Dosis', 20, 'bold'), bg='burlywood', width=32, bd=5)
        titulo_dgii.grid()

        # 2nd top panel

        top_panel_dgii2 = Frame(dgii_main, relief=RAISED, bd=1)
        top_panel_dgii2.pack(side=TOP, pady=20)

        # main buttons

        consult_rnc = Button(top_panel_dgii2, text='Consultar RNC', bd=3,
                             bg='gray', width=60, font=('Times New Roman', 12, 'bold'),
                             command=consult_1)
        consult_ncf = Button(top_panel_dgii2, text='Consultar NCF', bd=3,
                             bg='gray', width=60, font=('Times New Roman', 12, 'bold'),
                             command=consult_2)
        forms = Button(top_panel_dgii2, text='Formularios DGII', bd=3,
                       bg='gray', width=60, font=('Times New Roman', 12, 'bold'),
                       command=consult_forms)
        lista_buttons_dgii = [consult_rnc, consult_ncf, forms]

        counters = 0
        for titles in lista_buttons_dgii:
            titles.grid(row=counters, column=0)
            counters += 1

            if counters < 6:
                space = Label(top_panel_dgii2, text='', height=2)
                space.grid(row=counters, column=0)
                counters += 1

        # go back button

        texto_volver = Label(top_panel_dgii2, text='Volver atrás:',
                             font=('Times New Roman', 12, 'bold'))
        texto_volver.grid(row=6, column=0)

        boton_volver = Button(top_panel_dgii2, image=back_img, bd=3, command=volver_atras2)
        boton_volver.grid(row=7, column=0)

        # avoid terminate
        dgii_main.mainloop()

    # buttons variables & list
    cal_button = Button(left_panel, image=calculadora, bd=4, command=menu_calculator, height=136)
    dgii_button = Button(left_panel, image=dgii_icon, command=menu_dgii, bd=4, height=136)
    tss_button = Button(left_panel, image=tss_icon, bd=4, height=136)
    config_button = Button(left_panel, image=config_icon, bd=4, height=136)
    button_list = [cal_button, dgii_button, tss_button, config_button]

    # place main buttons
    counter = 0
    for buttons in button_list:
        # space between them
        espacio = Label(left_panel, text=' ', width=2, font=('Dosis', 27), bg='light grey')
        espacio.grid(row=0, column=counter, sticky=W)
        counter += 1

        # place main buttons
        buttons.grid(row=0, column=counter, pady=70, sticky=N)
        counter += 1

    # img titles/names
    img_names = ['Calculadora\nCalculator', 'Dirección Gral.\nImpuestos Int.',
                 'Tesorería de la\nSeguridad Soc.', 'Configuración\nConfiguration']
    counter2 = 1
    for names in img_names:
        img_titles = Label(left_panel, text=names, font=('Times New Roman', 14, 'bold'),
                           relief='raised', bg='burlywood', bd=1, height=2)
        img_titles.grid(row=1, column=counter2, sticky=N)
        counter2 += 2

    # avoid terminate
    mainapp.mainloop()


if __name__ == "__main__":
    main_a()


"""pyinstaller --name "Herramienta FC" --windowed --onefile --icon=img\\logo_ico.ico 
--hidden-import babel --hidden-import babel.numbers --hidden-import tkcalendar MainApp.py """
