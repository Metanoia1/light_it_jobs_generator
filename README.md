[yourfirm.herokuapp.com](https://yourfirm.herokuapp.com)

Нужно создать проект для управления рабочими.

Есть некоторые компании, они могут создавать рабочие места.

Есть рабочие которые могут наниматься на эти места.

У каждого рабочего есть скилы и рабочее место создается для рабочих с определенным(и) скилом(скилами).

У скила рабочего есть уровень от 1 до 5, на сколько хорошо он владеет скилом.

Рабочее место может создаваться с минимальным требуемым уровнем скила.

На одно рабочее место может требоваться более 1го рабочего.

У каждой компании есть 1 и более менеджеров.

Они могут создавать рабочие места для компании.

И также нанимать на эти места рабочих. т.е. они могут отсылать незанятым рабочим офферы.

Если рабочий принимает оффер он назначается на рабочее место. (для простоты он всегда начинает работать на следующий день после принятие оффера)

По окончанию рабочего дня рабочий обязан заполнять Time Sheet.

Time Sheet - это данные о дате и времени начала и конца рабочего дня (можно добавить начало/конец времени обеда).

Менеджер компании должен подтвердить или отклонить/исправить этот Time Sheet.

Каждый скил имеет базовое значение оплаты за 1 час.

Hапример, программист - 20$/час.

И каждый уровень скила добавляет фиксированную сумму к этому числу.

Например, каждый уровень программиста +5$/час.

Менеджер должен иметь возможность смотреть сколько нужно заплатить рабочему на каком-то рабочем месте.

Все действия должны логироваться.
