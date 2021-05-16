from problems.models import *
# test_user = users.objects.create(name = '', e_mail = '')
# test_project = Projects.objects.create(title = '', shortdescription = '', description = '', problem = '', analysis = '', curator = '')
test_project = Projects.objects.create(title = 'Интерактивный тур по НГУ',shortdescription = 'В связи с этим возникло следующее решение – систематизировать всю информацию о спецкурсах ММФ и представить её на одном ресурсе (на сайте нашего факультета, в новом разделе «Спецкурсы»).',description = ' Главной отличительной чертой нашего ресурса является автоматическая загрузка информации, то есть переданные с помощью специальной формы сведения в ходе работы алгоритма сохраняются на сайте, при этом это происходит без участия какого-либо человека.',problem = 'В последнее время студенты сталкиваются с такой проблемой: сведения о спецкурсах, размещенные на стенде или отдельных сайтах кафедр, являются устаревшими или недостаточно полными, чтобы можно было выбрать конкретный курс',analysis = 'На старом сайте ММФ НГУ было размещено более 160 спецкурсов и спецсеминаров. Сейчас есть два основных источника сведений о спецкурсах: доска объявлений, расположенная возле деканата ММФ НГУ, и сайты кафедр ММФ НГУ. Если рассматривать первый вариант, то найдены следующие недоработки: существуют объявления, которые уже неактуальны более одного года; некоторые кафедры ММФ НГУ разместили от себя не более 4 объявлений, что достаточно неинформативно. Сайты кафедр ММФ НГУ также содержат неактуальную информацию (за 2019-2020 учебный год и старше), или сведения о спецкурсах и спецсеминарах заполнены некорректным образом, так что записаться на них не представляется возможным. Причиной размещения устаревшей информации на ресурсах кафедр ММФ НГУ является отсутствие сотрудника, который занимается обновлением всех сведений, размещаемых на сайте. Также преподаватели вследствие возрастающей нагрузки физически не успевают это сделать.',curator = 'Еремкин Вячеслав Игоревич')