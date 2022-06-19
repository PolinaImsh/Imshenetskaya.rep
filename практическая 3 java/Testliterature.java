//Вариант 10). Литература
//        Literature:
//        Свойства:
//      - код источника литературы;
//      - Тип литературы;
//      - название;
//      - год издательства; - название издательства;
//      - количество страниц;
//      - автор;
public class Testliterature {
    public static void main(String[] args){
        literature literature = new literature(72346234, "Фентези", "Гарри Поттер и Философский камень", 1997, "Росмэн", 250, "Дж. Роулинг");
        System.out.println(literature.toString());
        System.out.println((literature));
    }
}
