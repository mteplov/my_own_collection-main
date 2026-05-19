#  Пользовательская Ansible Collection  
`my_own_namespace.yandex_cloud_elk`

##  Описание

Данный репозиторий содержит пользовательскую Ansible Collection, предназначенную для автоматизации задач конфигурации и развертывания компонентов **Yandex Cloud ELK (Elasticsearch, Logstash, Kibana)**.

Коллекция позволяет упростить управление инфраструктурой за счёт использования переиспользуемых ролей и кастомных модулей Ansible.

---

##  Установка

Коллекция использует кастомный модуль `file_creator`, поэтому устанавливается из собранного архива `.tar.gz`.

###  Установка из GitHub Releases

Скачайте архив коллекции:

 https://github.com/mteplov/my_own_collection-main/releases/tag/1.0.0

В разделе **Assets** загрузите файл:  
`my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz`

---

###  Установка через Ansible Galaxy

После скачивания выполните установку:

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
