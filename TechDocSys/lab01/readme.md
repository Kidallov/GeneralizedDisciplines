Код лабораторной работы:

```
% laboratory-work-01.tex
\documentclass[14pt]{extreport}

% --- Языки и шрифты (LuaLaTeX) ---
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{russian}
\setotherlanguages{english}

% Основной шрифт (если установлен в системе)
\setmainfont{Times New Roman}
% Если хотите подключить локальные шрифты, пример:
% \setmainfont[
%   Path=./fonts/,
%   Extension=.ttf,
%   Ligatures=TeX,
%   UprightFont={*-Regular},
%   BoldFont={*-Bold},
%   ItalicFont={*-Italic},
%   BoldItalicFont={*-BoldItalic}
% ]{BookmanOldStyle}
% \newfontfamily\cyrillicfont{BookmanOldStyle}[Path=./fonts/,Extension=.ttf,Script=Cyrillic]

% --- Поля и интервал (ГОСТ) ---
\usepackage[a4paper,left=30mm,right=10mm,top=20mm,bottom=20mm]{geometry}
\setlength{\parindent}{1.25cm} % красная строка
\setlength{\parskip}{0pt}
\usepackage{indentfirst} % делает отступ в первом абзаце раздела
\linespread{1.5} % полуторный интервал

% --- Графика, таблицы, формулы, гиперссылки ---
\usepackage{graphicx}
\usepackage{caption}
\usepackage{amsmath, amssymb}
\usepackage{hyperref}
\hypersetup{unicode=true, colorlinks=true, linkcolor=blue, urlcolor=blue}

% --- Дополнительно (если нужно) ---
\usepackage{float} % [H] для жёсткой позиции рисунков/таблиц
\usepackage{booktabs} % красивые линии в таблицах (опционально)

% --- Настройка заголовков страниц ---
% Титульная страница без номера, дальше - номера внизу по центру (plain)
\usepackage{fancyhdr}
\pagestyle{plain} % plain размещает номер по центру внизу
% (можно изменить стиль через fancyhdr, но plain удовлетворяет требованию "внизу по центру")

% --- Документ ---
\title{Реферат на тему: \\[0.4cm] \textbf{Автоматизированное рабочее место руководителя и специалистов: \\ Наглядное представление планов, полученных результатов, программных продуктов и другой информации}}
\author{Студент: Кидалов Александр Александрович \\ Группа: ХХ-00}
\date{\today}

\begin{document}

% ----- Титульная страница -----
\maketitle
\thispagestyle{empty} % убираем номер на титуле
\clearpage

% ----- Оглавление -----
\tableofcontents
\clearpage

% Начинаем нумерацию страниц с 1 (после титула)
\setcounter{page}{1}
\pagenumbering{arabic}
\pagestyle{plain}

% =======================
\chapter{Введение}
Здесь начинается текст введения. Введение знакомит читателя с предметом исследования, целью и задачами реферата.

Пример форматирования: \textbf{Жирный текст} может быть полезен для выделения важных терминов. \textit{Курсивный текст} используется для выделения цитат или названий. \underline{Подчёркнутый текст} применяется реже.

% Ссылка на внешний ресурс:
Более подробную информацию можно найти в Интернете по ссылке: \href{https://www.example.com}{Пример внешней ссылки}.

\chapter{Основная часть - 1}

\section{Раздел 1.1}
Текст первого раздела. Здесь можно описать концепцию автоматизированного рабочего места (АРМ), архитектуру, роли руководителя и специалистов.

\subsection{Подраздел 1.1.1}
Текст первого подраздела. Приведём иллюстрацию, отражающую архитектуру АРМ.

\subsection{Подраздел 1.1.2}
Текст второго подраздела.

\subsubsection{Подподраздел 1.1.2.1}
Текст подподраздела.

% -----------------------
\section{Раздел 2: Визуализация данных}
Описание подходов к визуализации планов и результатов: графики, таблицы, дашборды.

% --- Вставка рисунка ---
\begin{figure}[H]
  \centering
  % Поместите файл example-image.png в ту же папку, что и .tex файл
  \includegraphics[width=0.6\textwidth]{example-image.png}
  \caption{Пример иллюстрации архитектуры АРМ}
  \label{fig:arm}
\end{figure}

Ссылка на рисунок: см. рисунок \ref{fig:arm}.

% --- Таблица ---
\begin{table}[H]
  \centering
  \begin{tabular}{|c|c|c|}
    \hline
    Параметр & План & Результат \\
    \hline
    Задача 1 & Выполнить анализ & Выполнено \\
    \hline
    Задача 2 & Разработать модуль & В процессе \\
    \hline
  \end{tabular}
  \caption{Пример таблицы планов и результатов}
  \label{tab:plans}
\end{table}

Ссылка на таблицу: см. таблицу \ref{tab:plans}.

% --- Формулы (опционально) ---
\chapter{Математическая модель (опционально)}
Если необходимо, введите простую формулу:
\begin{equation}
E = mc^2
\end{equation}

И пример выравнивания нескольких уравнений:
\begin{align}\label{eq:myformula}
a &= b + c, \\
d &= e + f.
\end{align}
Ссылка на формулу: уравнение \eqref{eq:myformula}.

% =======================
\chapter{Заключение}
Здесь подводятся итоги. В заключении даются краткие выводы по проделанной работе, возможные направления дальнейшего развития проекта.

% =======================
\section{Список литературы}
\begin{enumerate}
  \item Иванов И.И. Название книги по визуализации. Издательство, 2019.
  \item Петров П.П. Статья об автоматизированных рабочих местах. Журнал «Информатика», 2020.
\end{enumerate}

% =======================
\end{document}
```

Результат выполненной работы: [Лабораторная_работа__1.pdf](https://github.com/user-attachments/files/22612414/_.__1.pdf)
