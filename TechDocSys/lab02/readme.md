# Лабораторная работа №2

## Код лабораторной работы:
```
\documentclass[11pt,a4paper,sans]{moderncv}

% ---- СТИЛЬ CV ----
\moderncvstyle{banking}    % стили: casual, classic, oldstyle, banking
\moderncvcolor{blue}       % цвета: blue, orange, green, red, purple, grey, black

% ---- КОДИРОВКА И ЯЗЫК ----
\usepackage{fontspec}
\defaultfontfeatures{Renderer=Basic, Ligatures=TeX}
\newfontfamily\cyrillicfonttt{CMU Typewriter Text}
\newfontfamily\cyrillicfont{CMU Sans Serif}
\setmainfont{CMU Sans Serif}
\setsansfont{CMU Sans Serif}
\setmonofont{CMU Typewriter Text}

\usepackage{polyglossia}
\setdefaultlanguage{russian}
\setotherlanguages{english}

% ---- ПОЛЯ ----
\usepackage[scale=0.9]{geometry}

% ---- ДАННЫЕ ----
\firstname{Александр}
\familyname{Кидалов}
\title{Curriculum Vitae}
\address{ул. Брянцева, д. 2}{г. Санкт-Петербург, Россия, 195269}
\phone[mobile]{+7~921~8793031}
\email{kidallovv@icloud.com}
\homepage{https://github.com/Kidallov}
\social[linkedin]{ivanov}

\begin{document}
\makecvtitle

% ---- ОБРАЗОВАНИЕ ----
\section{Образование}
\cventry{2023--2027}{Разработчик программного обеспечения}{Институт им. А. И. Герцена}{Санкт-Петербург}{Россия}{}

% ---- ОПЫТ РАБОТЫ ----
\section{Опыт работы}
\cventry{2025--наст. время}{Преподователь курсов}{ProGame}{Санкт-Петербург}{}{
    Преподование языков программирования: Python, JavaScript}

% ---- НАВЫКИ ----
\section{Навыки}
\cvitem{Языки программирования}{Python, JavaScript}
\cvitem{Технологии}{Linux, Git, Docker, SQL}
\cvitem{Языки}{Русский (родной), Английский (B2)}

% ---- ПРОЕКТЫ ----
\section{Проекты}
\cvitem{2024}{Разработка мобильного приложения для тренировки чтения (Kivy, Python)}

\clearpage
\end{document}
```
Результат данного кода представен в pdf формате: [Лабораторная_работа__2.pdf](https://github.com/user-attachments/files/22593700/_.__2.pdf)

