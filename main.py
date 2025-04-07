import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from math import pi

st.set_page_config(layout="wide", page_title="Финансовый Дэшборд Alphabet (Google)", page_icon="📊")

data = {
    2020: {
        'Revenues': 182527, 'Cost of Revenues': 84921, 'Research and development': 27573,
        'Sales and marketing': 19961, 'General and administrative': 12920, 'Operating Income': 41224,
        'Other income (expense), net': 11015, 'Income before income taxes': 52239,
        'Provision for income taxes': 7813, 'Net Income': 40269,
        'Earnings per share - basic': 59.61, 'Earnings per share - diluted': 58.61,
        'Weighted-average shares - basic': 675, 'Weighted-average shares - diluted': 687,
        'Cash and cash equivalents': 23736, 'Marketable securities': 115500,
        'Accounts receivable, net': 26587,
        'Inventory': 1254,
        'Other current assets': 7521,
        'Total Current Assets': 174598,
        'Property and equipment, net': 96885, 'Non-marketable investments': 26222,
        'Goodwill': 20924, 'Intangible assets, net': 3638,
        'Other non-current assets': 6917,
        'Total Non-Current Assets': 154586, 'Total Assets': 319616,
        'Accounts payable': 5749, 'Accrued expenses and other current liabilities': 46352,
        'Deferred revenue, current': 3234,
        'Total Current Liabilities': 55335, 'Long-term debt': 13938,
        'Deferred revenue, non-current': 1129, 'Other long-term liabilities': 28815,
        'Total Non-Current Liabilities': 43882, 'Total Liabilities': 99217,
        'Total Stockholders\' Equity': 220399,
        'Total Liabilities and Stockholders\' Equity': 319616,
        'Net cash provided by operating activities': 65124,
        'Net cash used in investing activities': -43373, 'Capital Expenditures': 22281,
        'Net cash provided by financing activities': -6020,
        'Net increase in cash and cash equivalents': 17829,
        'Google Services Revenue': 168635, 'Google Cloud Revenue': 13059, 'Other Bets Revenue': 657,
        'Hedging gains (losses) on revenues': 176,
        'Google Services Operating Income': 46048, 'Google Cloud Operating Loss': -5607,
        'Other Bets Operating Loss': -4476, 'Corporate costs, unallocated': -4741
    },
    2021: {
        'Revenues': 257637, 'Cost of Revenues': 110939, 'Research and development': 31562,
        'Sales and marketing': 26590, 'General and administrative': 17975, 'Operating Income': 78714,
        'Other income (expense), net': 12114, 'Income before income taxes': 90828,
        'Provision for income taxes': 14701, 'Net Income': 76033,
        'Earnings per share - basic': 113.96, 'Earnings per share - diluted': 112.20,
        'Weighted-average shares - basic': 667, 'Weighted-average shares - diluted': 678,
        'Cash and cash equivalents': 20945, 'Marketable securities': 118289,
        'Accounts receivable, net': 37000,
        'Inventory': 2100,
        'Other current assets': 10066,
        'Total Current Assets': 188400,
        'Property and equipment, net': 110972, 'Non-marketable investments': 28395,
        'Goodwill': 21176, 'Intangible assets, net': 3210,
        'Other non-current assets': 7010,
        'Total Non-Current Assets': 170763, 'Total Assets': 359268,
        'Accounts payable': 6102, 'Accrued expenses and other current liabilities': 55987,
        'Deferred revenue, current': 3993,
        'Total Current Liabilities': 66082, 'Long-term debt': 14777,
        'Deferred revenue, non-current': 1397, 'Other long-term liabilities': 24849,
        'Total Non-Current Liabilities': 41023, 'Total Liabilities': 107105,
        'Total Stockholders\' Equity': 252163,
        'Total Liabilities and Stockholders\' Equity': 359268,
        'Net cash provided by operating activities': 91652,
        'Net cash used in investing activities': -40349, 'Capital Expenditures': 24640,
        'Net cash provided by financing activities': -50169,
        'Net increase in cash and cash equivalents': -2791,
        'Google Services Revenue': 239333, 'Google Cloud Revenue': 19206, 'Other Bets Revenue': 753,
        'Hedging gains (losses) on revenues': -1655,
        'Google Services Operating Income': 89980, 'Google Cloud Operating Loss': -3097,
        'Other Bets Operating Loss': -5286, 'Corporate costs, unallocated': -2883
    },
    2022: {
        'Revenues': 282836, 'Cost of Revenues': 126203, 'Research and development': 39500,
        'Sales and marketing': 30581, 'General and administrative': 22156, 'Operating Income': 74842,
        'Other income (expense), net': -6022, 'Income before income taxes': 68820,
        'Provision for income taxes': 8890, 'Net Income': 59972,
        'Earnings per share - basic': 91.92, 'Earnings per share - diluted': 91.20,
        'Weighted-average shares - basic': 652, 'Weighted-average shares - diluted': 657,
        'Cash and cash equivalents': 21878, 'Marketable securities': 91966,
        'Accounts receivable, net': 39000,
        'Inventory': 2600,
        'Other current assets': 11102,
        'Total Current Assets': 166546,
        'Property and equipment, net': 123537, 'Non-marketable investments': 22727,
        'Goodwill': 23941, 'Intangible assets, net': 3025,
        'Other non-current assets': 10700,
        'Total Non-Current Assets': 183930, 'Total Assets': 365264,
        'Accounts payable': 5582, 'Accrued expenses and other current liabilities': 57413,
        'Deferred revenue, current': 4499,
        'Total Current Liabilities': 67494, 'Long-term debt': 14769,
        'Deferred revenue, non-current': 1567, 'Other long-term liabilities': 25468,
        'Total Non-Current Liabilities': 41804, 'Total Liabilities': 109298,
        'Total Stockholders\' Equity': 255966,
        'Total Liabilities and Stockholders\' Equity': 365264,
        'Net cash provided by operating activities': 91495,
        'Net cash used in investing activities': -39712, 'Capital Expenditures': 31476,
        'Net cash provided by financing activities': -69317,
        'Net increase in cash and cash equivalents': 933,
        'Google Services Revenue': 253553, 'Google Cloud Revenue': 26280, 'Other Bets Revenue': 1068,
        'Hedging gains (losses) on revenues': 1935,
        'Google Services Operating Income': 83878, 'Google Cloud Operating Loss': -2958,
        'Other Bets Operating Loss': -6146, 'Corporate costs, unallocated': 66
    },
    2023: {
        'Revenues': 307394, 'Cost of Revenues': 135460, 'Research and development': 45856,
        'Sales and marketing': 32253, 'General and administrative': 20907, 'Operating Income': 84293,
        'Other income (expense), net': 1163, 'Income before income taxes': 85456,
        'Provision for income taxes': 11715, 'Net Income': 73795,
        'Earnings per share - basic': 116.13, 'Earnings per share - diluted': 115.30,
        'Weighted-average shares - basic': 635, 'Weighted-average shares - diluted': 640,
        'Cash and cash equivalents': 25696, 'Marketable securities': 101977,
        'Accounts receivable, net': 42000,
        'Inventory': 2900,
        'Other current assets': 8846,
        'Total Current Assets': 181419,
        'Property and equipment, net': 130158, 'Non-marketable investments': 29797,
        'Goodwill': 24210, 'Intangible assets, net': 2824,
        'Other non-current assets': 10800,
        'Total Non-Current Assets': 197789, 'Total Assets': 402392,
        'Accounts payable': 7552, 'Accrued expenses and other current liabilities': 61934,
        'Deferred revenue, current': 5171,
        'Total Current Liabilities': 74657, 'Long-term debt': 13652,
        'Deferred revenue, non-current': 1847, 'Other long-term liabilities': 27568,
        'Total Non-Current Liabilities': 43067, 'Total Liabilities': 117724,
        'Total Stockholders\' Equity': 284668,
        'Total Liabilities and Stockholders\' Equity': 402392,
        'Net cash provided by operating activities': 101031,
        'Net cash used in investing activities': -44115, 'Capital Expenditures': 32334,
        'Net cash provided by financing activities': -61542,
        'Net increase in cash and cash equivalents': 3818,
        'Google Services Revenue': 284608, 'Google Cloud Revenue': 33088, 'Other Bets Revenue': 1526,
        'Hedging gains (losses) on revenues': -1828,
        'Google Services Operating Income': 96908, 'Google Cloud Operating Income': 1728,
        'Other Bets Operating Loss': -4119, 'Corporate costs, unallocated': -10224
    },
     2024: {
        'Revenues': 352742, 'Cost of Revenues': 155206, 'Research and development': 50441,
        'Sales and marketing': 35274, 'General and administrative': 22928, 'Operating Income': 108893,
        'Other income (expense), net': 2500, 'Income before income taxes': 111393,
        'Provision for income taxes': 16709, 'Net Income': 94684,
        'Earnings per share - basic': 151.50, 'Earnings per share - diluted': 149.90,
        'Weighted-average shares - basic': 625, 'Weighted-average shares - diluted': 631,
        'Cash and cash equivalents': 30000, 'Marketable securities': 110000,
        'Accounts receivable, net': 46000,
        'Inventory': 3300,
        'Other current assets': 10700,
        'Total Current Assets': 200000,
        'Property and equipment, net': 150000, 'Non-marketable investments': 32000,
        'Goodwill': 25000, 'Intangible assets, net': 2800,
        'Other non-current assets': 15000,
        'Total Non-Current Assets': 224800, 'Total Assets': 444800,
        'Accounts payable': 8500, 'Accrued expenses and other current liabilities': 68000,
        'Deferred revenue, current': 5700,
        'Total Current Liabilities': 82200, 'Long-term debt': 14000,
        'Deferred revenue, non-current': 2000, 'Other long-term liabilities': 29000,
        'Total Non-Current Liabilities': 45000, 'Total Liabilities': 127200,
        'Total Stockholders\' Equity': 317600,
        'Total Liabilities and Stockholders\' Equity': 444800,
        'Net cash provided by operating activities': 115000,
        'Net cash used in investing activities': -60000, 'Capital Expenditures': 45000,
        'Net cash provided by financing activities': -65000,
        'Net increase in cash and cash equivalents': -10000,
        'Google Services Revenue': 315000, 'Google Cloud Revenue': 42000, 'Other Bets Revenue': 1800,
        'Hedging gains (losses) on revenues': -500,
        'Google Services Operating Income': 108000, 'Google Cloud Operating Income': 4000,
        'Other Bets Operating Loss': -3500, 'Corporate costs, unallocated': -9607
    }
}


df_full = pd.DataFrame.from_dict(data, orient='index')
df_full.index.name = 'Год'
df_full.index = df_full.index.astype(int)

df_full['Google Cloud Operating Income/Loss'] = df_full['Google Cloud Operating Income'].fillna(df_full['Google Cloud Operating Loss'])
df_full.drop(columns=['Google Cloud Operating Income', 'Google Cloud Operating Loss'], errors='ignore', inplace=True)


st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Alphabet_Inc_logo.svg/1280px-Alphabet_Inc_logo.svg.png", use_container_width=True)
st.sidebar.title("Выполнил: Русинов Денис")
st.sidebar.title("🛠️ Настройки Дэшборда")
all_years = sorted(df_full.index.unique().tolist())
selected_years = st.sidebar.slider(
    "Выберите диапазон лет:",
    min_value=min(all_years),
    max_value=max(all_years),
    value=(min(all_years), max(all_years))
)

theme = st.sidebar.selectbox("Выберите тему графиков:", ('plotly', 'plotly_white', 'ggplot2', 'seaborn', 'simple_white'), index=1)

filtered_years = list(range(selected_years[0], selected_years[1] + 1))
df = df_full[df_full.index.isin(filtered_years)].copy()

df['Gross Profit'] = df['Revenues'] - df['Cost of Revenues']
df['Total Operating Expenses'] = df['Research and development'].fillna(0) + df['Sales and marketing'].fillna(0) + df['General and administrative'].fillna(0)

df['Revenue Growth (%)'] = df['Revenues'].pct_change() * 100
df['Net Income Growth (%)'] = df['Net Income'].pct_change() * 100
df['Operating Income Growth (%)'] = df['Operating Income'].pct_change() * 100
df['EPS Diluted Growth (%)'] = df['Earnings per share - diluted'].pct_change() * 100

df['Gross Margin (%)'] = (df['Gross Profit'] / df['Revenues'].replace(0, pd.NA)) * 100
df['Operating Margin (%)'] = (df['Operating Income'] / df['Revenues'].replace(0, pd.NA)) * 100
df['Net Margin (%)'] = (df['Net Income'] / df['Revenues'].replace(0, pd.NA)) * 100

df['Current Ratio'] = df['Total Current Assets'] / df['Total Current Liabilities'].replace(0, pd.NA)
df['Quick Ratio'] = (df['Cash and cash equivalents'].fillna(0) + df['Marketable securities'].fillna(0) + df.get('Accounts receivable, net', 0).fillna(0)) / df['Total Current Liabilities'].replace(0, pd.NA)
df['Cash Ratio'] = (df['Cash and cash equivalents'].fillna(0) + df['Marketable securities'].fillna(0)) / df['Total Current Liabilities'].replace(0, pd.NA)
df['Working Capital'] = df['Total Current Assets'].fillna(0) - df['Total Current Liabilities'].fillna(0)

df['Debt-to-Equity Ratio'] = df['Total Liabilities'] / df['Total Stockholders\' Equity'].replace(0, pd.NA)
df['Debt-to-Assets Ratio'] = df['Total Liabilities'] / df['Total Assets'].replace(0, pd.NA)
df['Equity Multiplier'] = df['Total Assets'] / df['Total Stockholders\' Equity'].replace(0, pd.NA)

df['Return on Assets (ROA) (%)'] = (df['Net Income'] / df['Total Assets'].shift(1).replace(0, pd.NA)) * 100
df['Return on Equity (ROE) (%)'] = (df['Net Income'] / df['Total Stockholders\' Equity'].shift(1).replace(0, pd.NA)) * 100

df['Effective Tax Rate (%)'] = (df['Provision for income taxes'] / df['Income before income taxes'].replace(0, pd.NA)) * 100
df['Operating Income Before Tax'] = df['Operating Income'] / (1 - df['Effective Tax Rate (%)'] / 100).replace(0, pd.NA)
df['Invested Capital'] = (df['Total Stockholders\' Equity'] + df['Long-term debt'].fillna(0)).shift(1)

df['Return on Invested Capital (ROIC) (%)'] = (df['Operating Income'] * (1 - df['Effective Tax Rate (%)'] / 100)) / df['Invested Capital'].replace(0, pd.NA) * 100


df['Asset Turnover'] = df['Revenues'] / df['Total Assets'].shift(1).replace(0, pd.NA)
df['Inventory Turnover'] = df['Cost of Revenues'] / df['Inventory'].shift(1).replace(0, pd.NA)
df['Receivables Turnover'] = df['Revenues'] / df['Accounts receivable, net'].shift(1).replace(0, pd.NA)

df['Free Cash Flow (FCF)'] = df['Net cash provided by operating activities'].fillna(0) - df['Capital Expenditures'].fillna(0)
df['FCF Growth (%)'] = df['Free Cash Flow (FCF)'].pct_change() * 100
df['FCF per Share'] = df['Free Cash Flow (FCF)'] * 1_000_000 / (df['Weighted-average shares - diluted'] * 1_000_000).replace(0, pd.NA)
df['FCF Margin (%)'] = (df['Free Cash Flow (FCF)'] / df['Revenues'].replace(0, pd.NA)) * 100

df['Book Value per Share'] = df['Total Stockholders\' Equity'] * 1_000_000 / (df['Weighted-average shares - diluted'] * 1_000_000).replace(0, pd.NA)
df['Revenue per Share'] = df['Revenues'] * 1_000_000 / (df['Weighted-average shares - diluted'] * 1_000_000).replace(0, pd.NA)

df['DuPont ROE Check (%)'] = (df['Net Margin (%)'] / 100) * df['Asset Turnover'] * df['Equity Multiplier'] * 100


def format_currency(value, millions=True):
    if pd.isna(value): return "N/A"
    abs_val = abs(value)
    sign = "-" if value < 0 else ""
    if millions:
        if abs_val >= 1_000_000:
            return f"{sign}${abs_val/1_000_000:,.1f}T"
        elif abs_val >= 1000:
            return f"{sign}${abs_val/1_000:,.1f}B"
        else:
             return f"{sign}${abs_val:,.0f}M"
    else:
        return f"{sign}${abs_val:,.2f}"

def format_percentage(value):
    if pd.isna(value): return "N/A"
    return f"{value:.1f}%"

def format_ratio(value):
     if pd.isna(value): return "N/A"
     return f"{value:.2f}x"

def format_per_share(value):
     if pd.isna(value): return "N/A"
     return f"${value:.2f}"

def format_dataframe(df_to_format):
    formatted_df = df_to_format.copy().astype(object)
    for idx in formatted_df.index:
        is_percent = '%' in idx
        is_ratio = 'Ratio' in idx or 'Turnover' in idx or 'Multiplier' in idx
        is_pershare = 'per Share' in idx or 'per share' in idx

        for col in formatted_df.columns:
            value = formatted_df.loc[idx, col]
            if pd.isna(value):
                formatted_df.loc[idx, col] = "N/A"
            elif is_percent:
                 formatted_df.loc[idx, col] = format_percentage(value)
            elif is_ratio:
                 formatted_df.loc[idx, col] = format_ratio(value)
            elif is_pershare:
                 formatted_df.loc[idx, col] = format_per_share(value)
            elif isinstance(value, (int, float)):
                  formatted_df.loc[idx, col] = format_currency(value)
    return formatted_df

def get_metric_color_and_tooltip(metric_name, value):
    color = "normal"
    tooltip = ""
    if pd.isna(value): return "inverse", "Нет данных"

    if metric_name == 'Current Ratio':
        if value >= 2.0: color = "off"; tooltip = "🟢 Отличная ликвидность (>= 2.0x)"
        elif value >= 1.0: color = "normal"; tooltip = "🟡 Достаточная ликвидность (1.0x-1.9x)"
        else: color = "inverse"; tooltip = "🔴 Низкая ликвидность (< 1.0x) - Потенциальный риск"
    elif metric_name == 'Quick Ratio':
        if value >= 1.0: color = "off"; tooltip = "🟢 Хорошая быстрая ликвидность (>= 1.0x)"
        else: color = "inverse"; tooltip = "🔴 Низкая быстрая ликвидность (< 1.0x) - Зависимость от медленно реализуемых активов"
    elif metric_name == 'Debt-to-Equity Ratio':
        if value <= 0.5: color = "off"; tooltip = "🟢 Низкая долговая нагрузка (<= 0.5x)"
        elif value <= 1.5: color = "normal"; tooltip = "🟡 Умеренная долговая нагрузка (0.5x-1.5x)"
        else: color = "inverse"; tooltip = "🔴 Высокая долговая нагрузка (> 1.5x) - Повышенный финансовый риск"
    elif metric_name == 'ROE (%)':
        if value >= 20: color = "off"; tooltip = "🟢 Высокая рентабельность капитала (>= 20%)"
        elif value >= 10: color = "normal"; tooltip = "🟡 Средняя рентабельность капитала (10-20%)"
        else: color = "inverse"; tooltip = "🔴 Низкая рентабельность капитала (< 10%)"
    elif metric_name == 'ROA (%)':
        if value >= 15: color = "off"; tooltip = "🟢 Высокая рентабельность активов (>= 15%)"
        elif value >= 5: color = "normal"; tooltip = "🟡 Средняя рентабельность активов (5-15%)"
        else: color = "inverse"; tooltip = "🔴 Низкая рентабельность активов (< 5%)"
    elif metric_name == 'Operating Margin (%)':
        if value >= 25: color = "off"; tooltip = "🟢 Высокая операционная маржа (>= 25%)"
        elif value >= 15: color = "normal"; tooltip = "🟡 Средняя операционная маржа (15-25%)"
        else: color = "inverse"; tooltip = "🔴 Низкая операционная маржа (< 15%)"
    elif metric_name == 'Net Margin (%)':
        if value >= 20: color = "off"; tooltip = "🟢 Высокая чистая маржа (>= 20%)"
        elif value >= 10: color = "normal"; tooltip = "🟡 Средняя чистая маржа (10-20%)"
        else: color = "inverse"; tooltip = "🔴 Низкая чистая маржа (< 10%)"

    return color, tooltip

def plot_gauge(value, title, max_value, reference=None):
    display_value = max(0, min(value, max_value)) if not pd.isna(value) else 0
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = display_value,
        number = {'valueformat': '.1f' if max_value > 5 else '.2f'},
        title = {'text': title, 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [0, max_value], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "cornflowerblue"},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "lightgray",
            'steps': [
                {'range': [0, max_value * 0.4], 'color': 'rgba(255, 128, 128, 0.5)'},
                {'range': [max_value * 0.4, max_value * 0.7], 'color': 'rgba(255, 255, 128, 0.5)'},
                {'range': [max_value * 0.7, max_value], 'color': 'rgba(128, 255, 128, 0.5)'}
                ],
            'threshold': {
                'line': {'color': "gray", 'width': 3},
                'thickness': 0.75,
                'value': reference} if reference is not None and not pd.isna(reference) else None
            }))
    fig.update_layout(height=200, margin={'t':30, 'b':10, 'l':10, 'r':10})
    return fig

st.title(f"📊 Финансовый Анализ Alphabet Inc. ({selected_years[0]}-{selected_years[1]})")
st.markdown("Дэшборд финансовой аналитики компании Alphabet в рамках дисциплины ДВФУ 'Визуализация экономических данных'*")

tab_titles = [
    "🌟 Обзор", "💰 P&L", "🏦 Баланс", "🌊 Денежный Поток",
    "🧩 Сегменты", "📈 Коэффициенты", "🔬 Доп. Анализ"
]
tabs = st.tabs(tab_titles)

if not df.empty:
    last_year = df.index.max()
    prev_year = last_year - 1 if last_year - 1 in df.index else None
else:
    last_year = max(all_years) if all_years else None
    prev_year = last_year - 1 if last_year else None
    df = pd.DataFrame()


with tabs[0]:
    st.header("🚀 Ключевые показатели (KPI)")
    if not df.empty and last_year is not None:
        col1, col2, col3, col4 = st.columns(4)
        revenue_last = df.loc[last_year, 'Revenues'] if 'Revenues' in df.columns else None
        revenue_delta = df.loc[last_year, 'Revenue Growth (%)'] if 'Revenue Growth (%)' in df.columns else None
        col1.metric("Годовая Выручка", format_currency(revenue_last) if revenue_last is not None else "N/A", format_percentage(revenue_delta) if revenue_delta is not None else None, help="Общий доход. Дельта = YoY рост.")
        net_income_last = df.loc[last_year, 'Net Income'] if 'Net Income' in df.columns else None
        net_income_delta = df.loc[last_year, 'Net Income Growth (%)'] if 'Net Income Growth (%)' in df.columns else None
        col2.metric("Чистая Прибыль", format_currency(net_income_last) if net_income_last is not None else "N/A", format_percentage(net_income_delta) if net_income_delta is not None else None, help="Прибыль после всех расходов и налогов. Дельта = YoY рост.")
        eps_last = df.loc[last_year, 'Earnings per share - diluted'] if 'Earnings per share - diluted' in df.columns else None
        eps_delta = df.loc[last_year, 'EPS Diluted Growth (%)'] if 'EPS Diluted Growth (%)' in df.columns else None
        col3.metric("EPS (Diluted)", format_per_share(eps_last) if eps_last is not None else "N/A", format_percentage(eps_delta) if eps_delta is not None else None, help="Прибыль на акцию (размытая). Дельта = YoY рост.")
        fcf_last = df.loc[last_year, 'Free Cash Flow (FCF)'] if 'Free Cash Flow (FCF)' in df.columns else None
        fcf_delta = df.loc[last_year, 'FCF Growth (%)'] if 'FCF Growth (%)' in df.columns else None
        col4.metric("Свободный Денежный Поток (FCF)", format_currency(fcf_last) if fcf_last is not None else "N/A", format_percentage(fcf_delta) if fcf_delta is not None else None, help="OCF минус CapEx. Дельта = YoY рост.")

        st.divider()
        st.subheader("📈 Динамика основных финансовых показателей")
        overview_metrics_options = ['Revenues', 'Operating Income', 'Net Income', 'Free Cash Flow (FCF)', 'Gross Profit']
        valid_overview_metrics = [m for m in overview_metrics_options if m in df.columns and df[m].notna().any()]
        default_overview_metrics = [m for m in ['Revenues', 'Operating Income', 'Net Income', 'Free Cash Flow (FCF)'] if m in valid_overview_metrics]

        overview_metrics_select = st.multiselect(
            "Выберите показатели для графика:",
            options=valid_overview_metrics,
            default=default_overview_metrics
        )
        if overview_metrics_select:
            fig_overview_trends = px.line(
                df, y=overview_metrics_select, title="Динамика выбранных показателей",
                labels={"value": "Сумма (млн $)", "variable": "Показатель", "Год": "Год"},
                markers=True, template=theme
            )
            fig_overview_trends.update_layout(hovermode="x unified")
            st.plotly_chart(fig_overview_trends, use_container_width=True)

        st.subheader(f"📊 Снимок коэффициентов за {last_year}")
        snapshot_cols = st.columns(5)
        snapshot_metrics = {
            'ROE (%)': (35, 20),
            'Operating Margin (%)': (40, 25),
            'Net Margin (%)': (35, 20),
            'Current Ratio': (4, 1.5),
            'Debt-to-Equity Ratio': (1, 0.5)
        }
        i = 0
        for metric, params in snapshot_metrics.items():
             if metric in df.columns:
                 value = df.loc[last_year, metric]
                 ref = params[1]
                 max_val = params[0]
                 if not pd.isna(value):
                     display_max_val = max(max_val, value * 1.2) if value > 0 else max_val
                     display_max_val = min(display_max_val, max_val * 2)

                     with snapshot_cols[i % 5]:
                          fig_gauge = plot_gauge(value, metric, display_max_val, ref)
                          st.plotly_chart(fig_gauge, use_container_width=True)
                          i += 1
        if i == 0:
             st.info("Нет данных для отображения моментальных снимков коэффициентов.")


        st.subheader("🌡️ Корреляция между ключевыми метриками")
        corr_metrics = ['Revenue Growth (%)', 'Operating Income Growth (%)', 'Net Income Growth (%)', 'FCF Growth (%)',
                        'Operating Margin (%)', 'Net Margin (%)', 'ROE (%)', 'ROA (%)']
        valid_corr_metrics = [m for m in corr_metrics if m in df.columns and df[m].notna().sum() > 1]
        if len(valid_corr_metrics) > 1:
            corr_matrix = df[valid_corr_metrics].corr()
            fig_heatmap = px.imshow(corr_matrix, text_auto=".2f", aspect="auto", color_continuous_scale='RdBu_r',
                                    title="Матрица корреляций", template=theme)
            fig_heatmap.update_layout(height=500)
            st.plotly_chart(fig_heatmap, use_container_width=True)

    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")


with tabs[1]:
    st.header("💰 Отчет о Прибылях и Убытках (Income Statement)")
    if not df.empty and last_year is not None:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader("Динамика доходов и расходов")
            is_area_metrics = ['Revenues', 'Gross Profit', 'Operating Income', 'Net Income']
            valid_is_area = [m for m in is_area_metrics if m in df.columns and df[m].notna().any()]
            if valid_is_area:
                fig_income_area = px.area(df, y=valid_is_area,
                                        title="Доходы и Прибыль (млн $)", labels={"value": "", "variable": "Статья"},
                                        template=theme, markers=False)
                fig_income_area.update_layout(hovermode="x unified")
                st.plotly_chart(fig_income_area, use_container_width=True)

        with col2:
            st.subheader(f"Структура OpEx ({last_year})")
            opex_cols = ['Research and development', 'Sales and marketing', 'General and administrative']
            valid_opex_cols = [c for c in opex_cols if c in df.columns and not pd.isna(df.loc[last_year, c])]
            if valid_opex_cols:
                last_year_data_opex = df.loc[[last_year], valid_opex_cols].T.reset_index()
                last_year_data_opex.columns = ['Расход', 'Сумма']
                last_year_data_opex = last_year_data_opex[last_year_data_opex['Сумма'] > 0]
                if not last_year_data_opex.empty:
                    fig_opex_structure = px.pie(last_year_data_opex, values='Сумма', names='Расход',
                                                title=f"Операционные Расходы ({last_year})", hole=0.4, template=theme)
                    fig_opex_structure.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05] * len(last_year_data_opex))
                    st.plotly_chart(fig_opex_structure, use_container_width=True)
                else:
                    st.info(f"Нет данных по структуре OpEx за {last_year}.")
            else:
                st.info(f"Нет данных по OpEx за {last_year}.")

        st.divider()
        col3, col4 = st.columns(2)
        with col3:
             st.subheader("Анализ Маржинальности (%)")
             margin_metrics = ['Gross Margin (%)', 'Operating Margin (%)', 'Net Margin (%)', 'FCF Margin (%)']
             valid_margin_metrics = [m for m in margin_metrics if m in df.columns and df[m].notna().any()]
             if valid_margin_metrics:
                 fig_margins = px.line(df[valid_margin_metrics], title="Динамика Маржинальности",
                                       labels={"value": "%", "variable": "Тип Маржи"}, markers=True, template=theme)
                 fig_margins.update_layout(hovermode="x unified")
                 st.plotly_chart(fig_margins, use_container_width=True)

        with col4:
            st.subheader(f"Водопад Прибыли ({last_year})")
            waterfall_cols = ['Revenues', 'Cost of Revenues', 'Gross Profit',
                              'Total Operating Expenses', 'Operating Income', 'Other income (expense), net',
                              'Income before income taxes', 'Provision for income taxes', 'Net Income']
            if all(c in df.columns for c in waterfall_cols) and not df.loc[[last_year], waterfall_cols].isna().any().any():
                values = [
                    df.loc[last_year, 'Revenues'], -df.loc[last_year, 'Cost of Revenues'], None,
                    -df.loc[last_year, 'Total Operating Expenses'], None, df.loc[last_year, 'Other income (expense), net'],
                    None, -df.loc[last_year, 'Provision for income taxes'], None
                ]
                measures = ["absolute", "relative", "total", "relative", "total", "relative", "total", "relative", "total"]
                labels = ["Выручка", "Себест.", "Валовая П.", "OpEx", "Опер. П.", "Прочее", "EBT", "Налоги", "Чистая П."]
                text_values = [format_currency(v) if v is not None else "" for v in values]

                calculated_values = []
                current_total = 0
                for i, v in enumerate(values):
                     if measures[i] == "absolute":
                          current_total = v
                          calculated_values.append(v)
                     elif measures[i] == "relative":
                          current_total += v
                          calculated_values.append(v)
                     elif measures[i] == "total":
                           calculated_values.append(current_total)
                           text_values[i] = format_currency(current_total)


                fig_waterfall = go.Figure(go.Waterfall(
                    name = str(last_year), orientation = "v", measure = measures,
                    x = labels, textposition = "outside", text = text_values,
                    y = calculated_values,
                    connector = {"line":{"color":"rgb(63, 63, 63)"}},
                ))
                fig_waterfall.update_layout(title=f"Структура Прибыли {last_year} (млн $)", template=theme, height=500)
                st.plotly_chart(fig_waterfall, use_container_width=True)
            else:
                st.info(f"Недостаточно данных для построения водопадной диаграммы за {last_year}.")


        st.subheader("Детализация Отчета о Прибылях и Убытках")
        income_statement_cols = [
            'Revenues', 'Cost of Revenues', 'Gross Profit', 'Research and development', 'Sales and marketing',
            'General and administrative', 'Total Operating Expenses', 'Operating Income', 'Other income (expense), net',
            'Income before income taxes', 'Provision for income taxes', 'Net Income',
            'Earnings per share - diluted', 'Revenue Growth (%)', 'Operating Margin (%)', 'Net Margin (%)'
        ]
        valid_is_cols = [col for col in income_statement_cols if col in df.columns]
        if valid_is_cols:
             df_to_display = df[valid_is_cols].T
             formatted_table = format_dataframe(df_to_display)
             st.dataframe(formatted_table, use_container_width=True)
        else:
            st.warning("Нет данных P&L для отображения в таблице.")


    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")


with tabs[2]:
    st.header("🏦 Балансовый отчет (Balance Sheet)")
    if not df.empty and last_year is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Активы vs Обязательства и Капитал")
            balance_metrics = ['Total Assets', 'Total Liabilities', 'Total Stockholders\' Equity']
            valid_balance_metrics = [m for m in balance_metrics if m in df.columns and df[m].notna().any()]
            if valid_balance_metrics:
                fig_balance_trends = px.line(df[valid_balance_metrics], title="Динамика Основных Компонентов Баланса",
                                             labels={"value": "Сумма (млн $)", "variable": "Компонент"}, markers=True, template=theme)
                fig_balance_trends.update_layout(hovermode="x unified")
                st.plotly_chart(fig_balance_trends, use_container_width=True)

            st.subheader("Капитальная структура")
            df['Debt'] = df['Long-term debt'].fillna(0)
            df['Equity'] = df['Total Stockholders\' Equity'].fillna(0)
            cap_structure_cols = ['Debt', 'Equity']
            if all(c in df.columns and df[c].notna().any() for c in cap_structure_cols):
                fig_cap_structure = px.area(df[cap_structure_cols], title="Долг vs Собственный Капитал",
                                            labels={"value": "Сумма (млн $)", "variable": "Компонент"}, template=theme)
                st.plotly_chart(fig_cap_structure, use_container_width=True)


        with col2:
            st.subheader(f"Структура Активов ({last_year})")
            asset_cols = ['Cash and cash equivalents', 'Marketable securities', 'Accounts receivable, net', 'Inventory', 'Other current assets',
                          'Property and equipment, net', 'Non-marketable investments', 'Goodwill', 'Intangible assets, net', 'Other non-current assets']
            valid_asset_cols = [c for c in asset_cols if c in df.columns and not pd.isna(df.loc[last_year, c]) and df.loc[last_year, c] > 0]
            if valid_asset_cols:
                asset_data = df.loc[last_year, valid_asset_cols]
                asset_df = pd.DataFrame({'Актив': asset_data.index, 'Сумма': asset_data.values})
                current_assets_list = ['Cash and cash equivalents', 'Marketable securities', 'Accounts receivable, net', 'Inventory', 'Other current assets']
                asset_df['Тип'] = asset_df['Актив'].apply(lambda x: 'Оборотные' if x in current_assets_list else 'Внеоборотные')

                fig_sunburst_assets = px.sunburst(asset_df, path=['Тип', 'Актив'], values='Сумма',
                                                 title=f"Детализация Активов ({last_year})", template=theme)
                fig_sunburst_assets.update_layout(margin = dict(t=40, l=0, r=0, b=0))
                st.plotly_chart(fig_sunburst_assets, use_container_width=True)
            else:
                 st.info(f"Нет данных по структуре активов за {last_year}.")


            st.subheader("Рабочий Капитал")
            if 'Working Capital' in df.columns and df['Working Capital'].notna().any():
                fig_wc = px.line(df, y='Working Capital', title="Динамика Рабочего Капитала",
                                 labels={"value": "Сумма (млн $)", "Год": "Год"}, markers=True, template=theme)
                st.plotly_chart(fig_wc, use_container_width=True)


        st.divider()
        st.subheader("🔬 Декомпозиция Баланса")
        balance_detail_options = {
            'Оборотные Активы': ['Cash and cash equivalents', 'Marketable securities', 'Accounts receivable, net', 'Inventory', 'Other current assets'],
            'Внеоборотные Активы': ['Property and equipment, net', 'Non-marketable investments', 'Goodwill', 'Intangible assets, net', 'Other non-current assets'],
            'Текущие Обязательства': ['Accounts payable', 'Accrued expenses and other current liabilities', 'Deferred revenue, current'],
            'Долгосрочные Обязательства': ['Long-term debt', 'Deferred revenue, non-current', 'Other long-term liabilities']
        }
        detail_choice = st.selectbox("Выберите категорию для детализации тренда:", list(balance_detail_options.keys()))
        detail_cols_valid = [col for col in balance_detail_options[detail_choice] if col in df.columns and df[col].notna().any()]
        if detail_cols_valid:
            fig_detail_trends = px.area(df[detail_cols_valid], title=f"Динамика: {detail_choice}",
                                       labels={"value": "Сумма (млн $)", "variable": "Статья", "Год": "Год"}, markers=False, template=theme)
            st.plotly_chart(fig_detail_trends, use_container_width=True)
        else:
             st.info(f"Нет данных для детализации категории '{detail_choice}'.")

        st.subheader("Детализация Балансового Отчета")
        balance_sheet_cols = [
            'Cash and cash equivalents', 'Marketable securities', 'Accounts receivable, net', 'Inventory', 'Other current assets', 'Total Current Assets',
            'Property and equipment, net', 'Non-marketable investments', 'Goodwill', 'Intangible assets, net', 'Other non-current assets', 'Total Non-Current Assets', 'Total Assets',
            'Accounts payable', 'Accrued expenses and other current liabilities', 'Deferred revenue, current', 'Total Current Liabilities',
            'Long-term debt', 'Deferred revenue, non-current', 'Other long-term liabilities', 'Total Non-Current Liabilities', 'Total Liabilities', 'Total Stockholders\' Equity'
        ]
        valid_bs_cols = [col for col in balance_sheet_cols if col in df.columns]
        if valid_bs_cols:
            df_to_display = df[valid_bs_cols].T
            formatted_table = format_dataframe(df_to_display)
            st.dataframe(formatted_table, use_container_width=True)
        else:
             st.warning("Нет данных Баланса для отображения в таблице.")
    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")

with tabs[3]:
    st.header("🌊 Отчет о Движении Денежных Средств (Cash Flow)")
    if not df.empty:
        st.subheader("Основные Денежные Потоки")
        cashflow_metrics = [
            'Net cash provided by operating activities', 'Net cash used in investing activities',
            'Net cash provided by financing activities', 'Net increase in cash and cash equivalents'
        ]
        valid_cf_metrics = [m for m in cashflow_metrics if m in df.columns and df[m].notna().any()]
        if valid_cf_metrics:
            df_cashflow_plot = df[valid_cf_metrics].copy()
            df_cashflow_plot.rename(columns={
                'Net cash provided by operating activities': 'Операционный (OCF)',
                'Net cash used in investing activities': 'Инвестиционный (ICF)',
                'Net cash provided by financing activities': 'Финансовый (FCF)',
                'Net increase in cash and cash equivalents': 'Чистое Изменение Денег'
            }, inplace=True)

            fig_cashflow_trends = px.bar(df_cashflow_plot, title="Денежные Потоки по Видам Деятельности",
                                         labels={"value": "Сумма (млн $)", "variable": "Тип Потока", "Год": "Год"}, template=theme)
            st.plotly_chart(fig_cashflow_trends, use_container_width=True)
        else:
             st.info("Нет данных по основным денежным потокам.")


        st.subheader("Операционный Поток, CapEx и Свободный Денежный Поток (FCF)")
        fcf_metrics_plot = ['Net cash provided by operating activities', 'Capital Expenditures', 'Free Cash Flow (FCF)']
        valid_fcf_metrics = [m for m in fcf_metrics_plot if m in df.columns and df[m].notna().any()]

        if len(valid_fcf_metrics) == 3:
            df_fcf_plot = df[valid_fcf_metrics].copy()
            df_fcf_plot['Capital Expenditures'] = -df_fcf_plot['Capital Expenditures'].fillna(0)
            df_fcf_plot.rename(columns={
                 'Net cash provided by operating activities': 'OCF', 'Capital Expenditures': 'CapEx', 'Free Cash Flow (FCF)': 'FCF'
            }, inplace=True)

            fig_fcf = go.Figure()
            fig_fcf.add_trace(go.Bar(x=df_fcf_plot.index, y=df_fcf_plot['OCF'], name='OCF', marker_color='rgb(55, 83, 109)'))
            fig_fcf.add_trace(go.Bar(x=df_fcf_plot.index, y=df_fcf_plot['CapEx'], name='CapEx', marker_color='rgb(26, 118, 255)'))
            fig_fcf.add_trace(go.Scatter(x=df_fcf_plot.index, y=df_fcf_plot['FCF'], name='FCF', mode='lines+markers', line=dict(color='firebrick', width=3)))
            fig_fcf.update_layout(title='OCF, CapEx и FCF (млн $)', xaxis_title='Год', yaxis_title='Сумма (млн $)',
                                  barmode='relative', template=theme, hovermode="x unified")
            st.plotly_chart(fig_fcf, use_container_width=True)
        else:
             st.info("Недостаточно данных для построения графика OCF vs CapEx vs FCF.")


        st.subheader("FCF на Акцию")
        if 'FCF per Share' in df.columns and df['FCF per Share'].notna().any():
            fig_fcf_ps = px.line(df, y='FCF per Share', title="Свободный Денежный Поток на Акцию",
                                 labels={"value": "$ на акцию", "Год": "Год"}, markers=True, template=theme)
            st.plotly_chart(fig_fcf_ps, use_container_width=True)

        st.subheader("Детализация Отчета о Движении Денежных Средств")
        cash_flow_cols = [
            'Net cash provided by operating activities', 'Capital Expenditures', 'Free Cash Flow (FCF)',
            'Net cash used in investing activities', 'Net cash provided by financing activities',
            'Net increase in cash and cash equivalents'
        ]
        valid_cf_cols = [col for col in cash_flow_cols if col in df.columns]
        if valid_cf_cols:
            df_to_display = df[valid_cf_cols].T
            formatted_table = format_dataframe(df_to_display)
            st.dataframe(formatted_table, use_container_width=True)
        else:
             st.warning("Нет данных ДДС для отображения в таблице.")
    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")


with tabs[4]:
    st.header("🧩 Сегментный Анализ")
    if not df.empty and last_year is not None:
        segment_revenue_cols = ['Google Services Revenue', 'Google Cloud Revenue', 'Other Bets Revenue']
        segment_opinc_cols = ['Google Services Operating Income', 'Google Cloud Operating Income/Loss',
                              'Other Bets Operating Loss', 'Corporate costs, unallocated']
        valid_rev_cols = [c for c in segment_revenue_cols if c in df.columns and df[c].notna().any()]
        valid_opinc_cols = [c for c in segment_opinc_cols if c in df.columns and df[c].notna().any()]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Выручка по Сегментам")
            if valid_rev_cols:
                fig_segment_rev = px.area(df[valid_rev_cols], title="Динамика Выручки по Сегментам (млн $)",
                                          labels={"value": "Выручка", "variable": "Сегмент", "Год": "Год"}, template=theme)
                st.plotly_chart(fig_segment_rev, use_container_width=True)

                st.subheader(f"Структура Выручки ({last_year})")
                last_year_rev_data = df.loc[[last_year], valid_rev_cols].T.reset_index()
                last_year_rev_data.columns = ['Сегмент', 'Выручка']
                last_year_rev_data = last_year_rev_data[last_year_rev_data['Выручка'] > 0]
                if not last_year_rev_data.empty:
                     fig_pie_rev = px.pie(last_year_rev_data, values='Выручка', names='Сегмент',
                                     title=f"Доли Сегментов в Выручке {last_year}", hole=0.4, template=theme)
                     fig_pie_rev.update_traces(textposition='inside', textinfo='percent+label')
                     st.plotly_chart(fig_pie_rev, use_container_width=True)
                else:
                     st.info(f"Нет данных по структуре выручки сегментов за {last_year}.")
            else:
                 st.info("Нет данных по выручке сегментов.")


        with col2:
            st.subheader("Операционная Прибыль/Убыток")
            if valid_opinc_cols:
                df_opinc_plot = df[valid_opinc_cols].reset_index()
                df_opinc_melt = df_opinc_plot.melt(id_vars=['Год'], var_name='Сегмент', value_name='Прибыль/Убыток')

                fig_segment_opinc = px.bar(df_opinc_melt, x='Год', y='Прибыль/Убыток', color='Сегмент',
                                           title="Опер. Прибыль (Убыток) по Сегментам (млн $)", template=theme,
                                           labels={"Прибыль/Убыток": "Сумма (млн $)", "Год": "Год"})
                st.plotly_chart(fig_segment_opinc, use_container_width=True)

                st.subheader(f"Структура Опер. Прибыли ({last_year})")
                last_year_opinc_data = df.loc[last_year, valid_opinc_cols].copy()
                profitable_segments = last_year_opinc_data[(last_year_opinc_data > 0) & (~last_year_opinc_data.index.isin(['Corporate costs, unallocated']))]

                if not profitable_segments.empty:
                    opinc_df = pd.DataFrame({'Сегмент': profitable_segments.index, 'Прибыль': profitable_segments.values})
                    fig_pie_opinc = px.pie(opinc_df, values='Прибыль', names='Сегмент',
                                            title=f"Вклад в Положительную Опер. Прибыль {last_year}", hole=0.4, template=theme)
                    fig_pie_opinc.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig_pie_opinc, use_container_width=True)
                else:
                    st.info(f"В {last_year} не было нескольких сегментов с положительной операционной прибылью для отображения структуры.")
            else:
                 st.info("Нет данных по операционной прибыли сегментов.")


        st.subheader("Детализация по Сегментам")
        segment_cols = valid_rev_cols + valid_opinc_cols
        if segment_cols:
             existing_segment_cols = [col for col in segment_cols if col in df.columns]
             if existing_segment_cols:
                 df_to_display = df[existing_segment_cols].T
                 formatted_table = format_dataframe(df_to_display)
                 st.dataframe(formatted_table, use_container_width=True)
             else:
                  st.warning("Нет данных по сегментам для отображения в таблице.")
        else:
             st.warning("Нет колонок сегментов для отображения.")

    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")


with tabs[5]:
    st.header("📈 Финансовые Коэффициенты")
    if not df.empty and last_year is not None:
        ratio_categories = {
            "Рентабельность": ['Gross Margin (%)', 'Operating Margin (%)', 'Net Margin (%)', 'FCF Margin (%)', 'Return on Assets (ROA) (%)', 'Return on Equity (ROE) (%)', 'Return on Invested Capital (ROIC) (%)'],
            "Ликвидность": ['Current Ratio', 'Quick Ratio', 'Cash Ratio', 'Working Capital'],
            "Платежеспособность": ['Debt-to-Equity Ratio', 'Debt-to-Assets Ratio', 'Equity Multiplier'],
            "Эффективность": ['Asset Turnover', 'Inventory Turnover', 'Receivables Turnover'],
            "На Акцию": ['Earnings per share - diluted', 'Book Value per Share', 'Revenue per Share', 'FCF per Share']
        }

        col1, col2 = st.columns([1,3])
        with col1:
            st.subheader("Категории")
            available_categories = {}
            for cat, metrics in ratio_categories.items():
                 if any(m in df.columns and df[m].notna().any() for m in metrics):
                      available_categories[cat] = metrics

            if available_categories:
                 selected_category = st.radio("Выберите категорию:", list(available_categories.keys()), label_visibility="collapsed")
            else:
                 selected_category = None
                 st.info("Нет доступных категорий коэффициентов.")


            st.markdown("---")
            st.subheader("DuPont Анализ ROE")
            dupont_cols = ['Net Margin (%)', 'Asset Turnover', 'Equity Multiplier', 'ROE (%)']
            valid_dupont = [c for c in dupont_cols if c in df.columns and df[c].notna().any()]
            if len(valid_dupont) == len(dupont_cols):
                 df_dupont_display = df[valid_dupont].copy()
                 formatted_dupont = df_dupont_display.copy().astype(object)
                 for idx in formatted_dupont.index:
                     formatted_dupont.loc[idx, 'Net Margin (%)'] = format_percentage(df_dupont_display.loc[idx, 'Net Margin (%)'])
                     formatted_dupont.loc[idx, 'Asset Turnover'] = format_ratio(df_dupont_display.loc[idx, 'Asset Turnover'])
                     formatted_dupont.loc[idx, 'Equity Multiplier'] = format_ratio(df_dupont_display.loc[idx, 'Equity Multiplier'])
                     formatted_dupont.loc[idx, 'ROE (%)'] = format_percentage(df_dupont_display.loc[idx, 'ROE (%)'])

                 st.dataframe(formatted_dupont, column_config={"_index":"Год"})
                 st.caption("ROE ≈ Чист.Маржа × Оборач.Активов × Фин.Рычаг")
            else:
                 st.caption("Недостаточно данных для полного DuPont анализа.")


        with col2:
            if selected_category:
                st.subheader(f"Динамика: {selected_category}")
                metrics_to_plot = [metric for metric in available_categories[selected_category] if metric in df.columns and df[metric].notna().any()]
                if metrics_to_plot:
                    plot_wc_separately = 'Working Capital' in metrics_to_plot and len(metrics_to_plot) > 1
                    if plot_wc_separately:
                         metrics_to_plot.remove('Working Capital')


                    if metrics_to_plot:
                        fig_ratios = px.line(df[metrics_to_plot], title=f"Динамика Коэффициентов ({selected_category})",
                                             labels={"value": "Значение", "variable": "Коэффициент", "Год": "Год"}, markers=True, template=theme)
                        fig_ratios.update_layout(hovermode="x unified")
                        st.plotly_chart(fig_ratios, use_container_width=True)

                    if plot_wc_separately and 'Working Capital' in df.columns and df['Working Capital'].notna().any():
                         fig_wc_trend = px.line(df[['Working Capital']], title="Динамика Рабочего Капитала", markers=True, template=theme,
                                                labels={"value": "Сумма (млн $)", "Год": "Год"})
                         st.plotly_chart(fig_wc_trend, use_container_width=True)


                    st.subheader(f"Значения за {last_year}")
                    all_metrics_in_cat = [m for m in available_categories[selected_category] if m in df.columns]
                    ratio_metric_cols = st.columns(min(len(all_metrics_in_cat), 4))
                    col_idx = 0
                    for metric in all_metrics_in_cat:
                        if metric not in df.columns: continue
                        value = df.loc[last_year, metric]
                        delta_val = None
                        if prev_year in df.index and metric in df.columns:
                             prev_value = df.loc[prev_year, metric]
                             if not pd.isna(value) and not pd.isna(prev_value):
                                  delta_val = value - prev_value


                        color, tooltip = get_metric_color_and_tooltip(metric, value)

                        with ratio_metric_cols[col_idx % len(ratio_metric_cols)]:
                             formatted_val = "N/A"
                             if not pd.isna(value):
                                  if '%' in metric: formatted_val = format_percentage(value)
                                  elif 'Ratio' in metric or 'Turnover' in metric or 'Multiplier' in metric: formatted_val = format_ratio(value)
                                  elif 'per Share' in metric: formatted_val = format_per_share(value)
                                  else: formatted_val = format_currency(value)

                             delta_str = None
                             delta_color="normal"
                             if delta_val is not None:
                                 delta_str = f"{delta_val:+.2f}"
                                 if '%' not in metric and 'Ratio' not in metric and 'Turnover' not in metric and 'Multiplier' not in metric and 'per Share' not in metric:
                                      delta_str = format_currency(delta_val)
                                 delta_color="normal" if delta_val == 0 else ("off" if delta_val > 0 else "inverse")


                             st.metric(label=metric, value=formatted_val,
                                       delta=delta_str,
                                       delta_color=delta_color,
                                       help=tooltip if tooltip else f"Изменение с {prev_year}г.")
                        col_idx += 1
                else:
                    st.warning(f"Нет данных для отображения коэффициентов в категории '{selected_category}'.")
            else:
                 st.info("Выберите категорию слева для просмотра коэффициентов.")


        st.markdown("---")
        st.info("ℹ️ **Интерпретация:** Сравнивайте коэффициенты с историческими значениями, отраслевыми бенчмарками и конкурентами. Учитывайте контекст (например, стадию роста компании, экономическую ситуацию). 2024 год - прогноз.")

    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")


with tabs[6]:
    st.header("🔬 Дополнительный Анализ и Сводка")
    if not df.empty:
        st.subheader("⚙️ Взаимосвязь Показателей")
        col1, col2 = st.columns(2)
        with col1:
             x_axis_options = ['Research and development', 'Sales and marketing', 'Capital Expenditures', 'Revenue Growth (%)', 'Revenues']
             valid_x_options = [o for o in x_axis_options if o in df.columns and df[o].notna().any()]
             x_axis = st.selectbox("Выберите ось X:", valid_x_options if valid_x_options else ["Нет опций"])
        with col2:
             y_axis_options = ['Operating Margin (%)', 'Net Margin (%)', 'ROE (%)', 'FCF Margin (%)', 'Operating Income Growth (%)', 'Net Income Growth (%)']
             valid_y_options = [o for o in y_axis_options if o in df.columns and df[o].notna().any()]
             y_axis = st.selectbox("Выберите ось Y:", valid_y_options if valid_y_options else ["Нет опций"])

        if x_axis != "Нет опций" and y_axis != "Нет опций":
             size_col = 'Revenues' if 'Revenues' in df.columns and df['Revenues'].notna().any() else None
             color_col = 'Operating Margin (%)' if 'Operating Margin (%)' in df.columns and df['Operating Margin (%)'].notna().any() else None

             hover_data_cols = ['Revenues', 'Net Income']
             valid_hover_cols = [c for c in hover_data_cols if c in df.columns]

             fig_scatter = px.scatter(df.reset_index(), x=x_axis, y=y_axis, text='Год',
                                     size=size_col, color=color_col,
                                     hover_name='Год', hover_data=valid_hover_cols,
                                     title=f'Взаимосвязь: {x_axis} vs {y_axis}', template=theme,
                                     labels={x_axis: f"{x_axis}", y_axis: f"{y_axis}"})
             fig_scatter.update_traces(textposition='top center', textfont_size=10)
             fig_scatter.update_layout(height=500)
             st.plotly_chart(fig_scatter, use_container_width=True)

        st.subheader("📊 Сводка по Ключевым Трендам (CAGR)")
        if len(df) > 1:
            start_year = df.index.min()
            end_year = df.index.max()
            num_years = end_year - start_year

            cagr_metrics = ['Revenues', 'Operating Income', 'Net Income', 'Free Cash Flow (FCF)', 'Earnings per share - diluted']
            cagr_results = {}
            if num_years > 0:
                 for metric in cagr_metrics:
                    if metric in df.columns:
                        start_value = df.loc[start_year, metric]
                        end_value = df.loc[end_year, metric]
                        if not pd.isna(start_value) and not pd.isna(end_value) and start_value != 0 and end_value > 0:
                             sign = -1 if start_value < 0 else 1
                             cagr = ((end_value / start_value) ** (1 / num_years)) - 1
                             cagr = sign * ( (abs(end_value / start_value))**(1/num_years) -1 )
                             cagr_results[f"{metric} CAGR ({start_year}-{end_year})"] = format_percentage(cagr * 100)
                        else:
                             cagr_results[f"{metric} CAGR ({start_year}-{end_year})"] = "N/A"
                 if cagr_results:
                     st.dataframe(pd.Series(cagr_results), column_config={"value":"CAGR"})
                 else:
                      st.info("Не удалось рассчитать CAGR для ключевых метрик.")

            else:
                 st.info("Требуется более одного года для расчета CAGR.")

        else:
            st.info("Требуется более одного года для расчета CAGR.")

        st.subheader("📝 Общие Выводы (Автоматизированные)")
        conclusions = []
        if 'Revenue Growth (%)' in df.columns and df['Revenue Growth (%)'].notna().any():
            avg_rev_growth = df['Revenue Growth (%)'].mean()
            if not pd.isna(avg_rev_growth):
                 if avg_rev_growth > 15: conclusions.append(f"📈 Стабильно высокий рост выручки (средний YoY: {format_percentage(avg_rev_growth)}).")
                 elif avg_rev_growth > 5: conclusions.append(f"📈 Умеренный рост выручки (средний YoY: {format_percentage(avg_rev_growth)}).")
                 else: conclusions.append(f"📉 Рост выручки замедлился или отсутствует (средний YoY: {format_percentage(avg_rev_growth)}).")
        if 'Net Margin (%)' in df.columns and df['Net Margin (%)'].notna().any():
            avg_net_margin = df['Net Margin (%)'].mean()
            if not pd.isna(avg_net_margin):
                 if avg_net_margin > 20: conclusions.append(f"💰 Очень высокая чистая рентабельность (в среднем {format_percentage(avg_net_margin)}).")
                 elif avg_net_margin > 10: conclusions.append(f"💰 Хорошая чистая рентабельность (в среднем {format_percentage(avg_net_margin)}).")
                 else: conclusions.append(f"📉 Рентабельность требует внимания (в среднем {format_percentage(avg_net_margin)}).")
        if 'FCF Margin (%)' in df.columns and df['FCF Margin (%)'].notna().any():
            avg_fcf_margin = df['FCF Margin (%)'].mean()
            if not pd.isna(avg_fcf_margin):
                if avg_fcf_margin > 15: conclusions.append(f"🌊 Сильная генерация свободного денежного потока (FCF Маржа > 15%).")
                else: conclusions.append(f"🌊 Генерация FCF умеренная (FCF Маржа < 15%).")
        if 'Debt-to-Equity Ratio' in df.columns and df['Debt-to-Equity Ratio'].notna().any():
            avg_de_ratio = df['Debt-to-Equity Ratio'].mean()
            if not pd.isna(avg_de_ratio):
                 if avg_de_ratio < 0.5: conclusions.append(f"🏦 Крепкий баланс с низкой долговой нагрузкой (D/E < 0.5x).")
                 else: conclusions.append(f"🏦 Долговая нагрузка умеренная или повышенная (D/E > 0.5x).")

        if conclusions:
            for conclusion in conclusions:
                st.markdown(f"- {conclusion}")
        else:
            st.info("Недостаточно данных для генерации автоматических выводов.")

        if 2024 in df.index:
             st.markdown(f"- ⚠️ **Помните:** Данные за 2024 год являются прогнозными и могут отличаться от фактических результатов.")

    else:
        st.warning("Нет данных для отображения в выбранном диапазоне лет.")

st.sidebar.divider()
st.sidebar.info("Дэшборд разработан с использованием Streamlit & Plotly.")
st.sidebar.markdown(f"Период анализа: **{selected_years[0]}-{selected_years[1]}**")
st.sidebar.caption(f"Текущая дата: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")