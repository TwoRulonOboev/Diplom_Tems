# Автоматизированный перевод и стилистическая корректировка текста с использованием нейронных сетей

<details>
  <summary><h2>Описание проекта</h2></summary>
  <p>Проект направлен на создание системы, которая выполняет автоматический перевод текста и его стилистическую корректировку в зависимости от выбранного жанра или стиля. Пользователь загружает исходный файл на сайт, выбирает целевой стиль (научный, художественный, технический и т.д.), и система выполняет перевод с последующей адаптацией текста под заданные требования. После обработки пользователь может скачать готовый документ.</p>
</details>

<details>
  <summary><h2>Основная идея</h2></summary>
  <p>Идея проекта заключается в интеграции машинного перевода и стилистической обработки текста, что позволяет пользователям получать не только качественный перевод, но и текст, соответствующий требуемым стилевым стандартам.</p>
</details>

<details>
  <summary><h2>Распределение задач</h2></summary>

  <details>
    <summary><h2>Участник 1: Разработка веб-сайта и API для загрузки файлов, взаимодействие с модулем нейронной сети</h2></summary>
    <h3>Задачи:</h3>
    <ul>
      <li><strong>Разработка веб-интерфейса:</strong>
        <ul>
          <li>Создание сайта для загрузки файлов (.docx, .pdf, .txt и т.д.).</li>
          <li>Интерфейс выбора стиля для перевода (технический, научный, художественный и др.).</li>
          <li>Информация о процессе обработки и возможность скачивания результатов.</li>
        </ul>
      </li>
      <li><strong>Обработка файлов на сервере:</strong>
        <ul>
          <li>Конвертация загруженных файлов в текстовый формат.</li>
          <li>Поддержка работы с форматами .docx, .pdf и другими для их корректной обработки.</li>
        </ul>
      </li>
      <li><strong>API для взаимодействия с нейронной сетью:</strong>
        <ul>
          <li>Реализация REST API для передачи текста в модуль перевода и корректировки.</li>
          <li>Получение результатов от нейронной сети и возврат обработанного текста.</li>
        </ul>
      </li>
      <li><strong>Функции безопасности и хранения данных:</strong>
        <ul>
          <li>Шифрование данных и файлов.</li>
          <li>Защита загруженных файлов и данных пользователей.</li>
        </ul>
      </li>
    </ul>
    <h3>Технологии для изучения:</h3>
    <ul>
      <li><strong>Frontend:</strong> HTML, CSS, JavaScript (React, Vue.js, Angular).</li>
      <li><strong>Backend:</strong> Python (Flask, Django) или Node.js.</li>
      <li><strong>Работа с файлами:</strong> python-docx, PyPDF2.</li>
      <li><strong>API взаимодействие:</strong> RESTful API.</li>
      <li><strong>Безопасность:</strong> SSL-сертификаты, шифрование данных.</li>
    </ul>
  </details>

  <details>
    <summary><h2>Участник 2: Разработка нейронной сети для перевода и стилистической адаптации текста</h2></summary>
    <h3>Задачи:</h3>
    <ul>
      <li><strong>Перевод текста с помощью нейронной сети:</strong>
        <ul>
          <li>Использование предобученных моделей перевода (BART, MarianMT).</li>
        </ul>
      </li>
      <li><strong>Стилистическая адаптация текста:</strong>
        <ul>
          <li>Разработка модуля для анализа стиля текста и адаптации перевода под указанный стиль.</li>
        </ul>
      </li>
      <li><strong>Обучение и настройка модели:</strong>
        <ul>
          <li>Fine-tuning предобученных моделей для улучшения перевода и адаптации.</li>
          <li>Сбор и разметка данных для обучения.</li>
        </ul>
      </li>
      <li><strong>Интеграция с API:</strong>
        <ul>
          <li>Взаимодействие с серверной частью через API.</li>
          <li>Оптимизация моделей для работы с большими объемами данных.</li>
        </ul>
      </li>
    </ul>
    <h3>Технологии для изучения:</h3>
    <ul>
      <li><strong>Машинное обучение и NLP:</strong>
        <ul>
          <li>Hugging Face Transformers (BART, MarianMT, T5).</li>
          <li>PyTorch или TensorFlow.</li>
          <li>NLP библиотеки (spaCy, NLTK).</li>
        </ul>
      </li>
      <li><strong>Обучение моделей:</strong>
        <ul>
          <li>Fine-tuning на основе данных различных стилей (технические, научные тексты и др.).</li>
          <li>Оптимизация для работы с большими объемами данных.</li>
        </ul>
      </li>
    </ul>
  </details>
</details>

<details>
  <summary><h2>Детализированное описание процесса:</h2></summary>
  <ol>
    <li><strong>Пользователь загружает файл на сайт:</strong>
      <ul>
        <li>Выбор файла и стиля перевода.</li>
        <li>Опциональный выбор языка перевода.</li>
      </ul>
    </li>
    <li><strong>Передача текста на сервер:</strong>
      <ul>
        <li>Файл конвертируется в текстовый формат и передается в нейронную сеть.</li>
      </ul>
    </li>
    <li><strong>Перевод текста:</strong>
      <ul>
        <li>Модель переводит текст с использованием предобученных моделей.</li>
      </ul>
    </li>
    <li><strong>Стилистическая корректировка:</strong>
      <ul>
        <li>Модель адаптирует текст под выбранный стиль.</li>
      </ul>
    </li>
    <li><strong>Возвращение результата:</strong>
      <ul>
        <li>Обработанный текст возвращается пользователю для скачивания.</li>
      </ul>
    </li>
  </ol>
</details>

<details>
  <summary><h2>Возможные сложности и решения:</h2></summary>
  
  <ul>
    <li><strong>Обучение моделей на разных стилях:</strong>
      <ul>
        <li>Использование готовых датасетов и fine-tuning моделей.</li>
      </ul>
    </li>
    <li><strong>Перевод сложных терминов:</strong>
      <ul>
        <li>Сбор специализированных словарей.</li>
      </ul>
    </li>
    <li><strong>Интеграция перевода и стилистической адаптации:</strong>
      <ul>
        <li>Оптимизация пайплайна обработки текста.</li>
      </ul>
    </li>
    <li><strong>Обработка больших файлов:</strong>
      <ul>
        <li>Параллельная обработка текста и оптимизация моделей.</li>
      </ul>
    </li>
  </ul>
</details>

<details>
  <summary><h2>Ресурсы для изучения технологий</h2></summary>

  <h3>Участник 1 (веб-разработка, API, обработка файлов):</h3>
  <ul>
    <li>Flask документация: <a href="https://flask.palletsprojects.com/en/2.0.x/">https://flask.palletsprojects.com/en/2.0.x/</a></li>
    <li>Django документация: <a href="https://docs.djangoproject.com/en/4.0/">https://docs.djangoproject.com/en/4.0/</a></li>
    <li>Python-docx для работы с .docx файлами: <a href="https://python-docx.readthedocs.io/en/latest/">https://python-docx.readthedocs.io/en/latest/</a></li>
    <li>PyPDF2 для работы с PDF: <a href="https://pythonhosted.org/PyPDF2/">https://pythonhosted.org/PyPDF2/</a></li>
    <li>Google Cloud Translation API: <a href="https://cloud.google.com/translate/docs">https://cloud.google.com/translate/docs</a></li>
  </ul>

  <h3>Участник 2 (нейронные сети, машинное обучение, NLP):</h3>
  <ul>
    <li>Hugging Face Transformers документация: <a href="https://huggingface.co/transformers/">https://huggingface.co/transformers/</a></li>
    <li>PyTorch документация: <a href="https://pytorch.org/">https://pytorch.org/</a></li>
    <li>TensorFlow документация: <a href="https://www.tensorflow.org/">https://www.tensorflow.org/</a></li>
    <li>SpaCy документация: <a href="https://spacy.io/">https://spacy.io/</a></li>
    <li>NLTK документация: <a href="https://www.nltk.org/">https://www.nltk.org/</a></li>
  </ul>
</details>
