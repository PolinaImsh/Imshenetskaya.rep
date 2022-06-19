//Вариант 10). Литература
//        Literature:
//        Свойства:
//      - код источника литературы;
//      - Тип литературы;
//      - название;
//      - год издательства; - название издательства;
//      - количество страниц;
//      - автор;
public class literature {
    private int SourceCode;
    private String TypeLiterature;
    private String Name;
    private int YearPublishing;
    private String NamePublishing;
    private int Pages;
    private String Author;

    public literature(int SourceCode, String TypeLiterature, String Name, int YearPublishing, String NamePublishing, int Pages, String Author){
        this.SourceCode = SourceCode;
        this.TypeLiterature = TypeLiterature;
        this.Name = Name;
        this.YearPublishing = YearPublishing;
        this.NamePublishing = NamePublishing;
        this.Pages = Pages;
        this.Author = Author;
    }
    public int getSourceCode(){
        return SourceCode;
    }
    public void setSourceCode(int SourceCode){
        this.SourceCode = SourceCode;
    }
    public String getTypeLiterature(){
        return TypeLiterature;
    }
    public void setTypeLiterature(String TypeLiterature) {
        this.TypeLiterature = TypeLiterature;
    }
    public String getName(){
        return Name;
    }
    public void setName(String Name){
        this.Name = Name;
    }
    public int getYearPublishing(){
        return YearPublishing;
    }
    public void setYearPublishing(int YearPublishing){
        this.YearPublishing = YearPublishing;
    }
    public String getNamePublishing(){
        return NamePublishing;
    }
    public void setNamePublishing(String NamePublishing){
        this.NamePublishing = NamePublishing;
    }
    public int getPages(){
        return Pages;
    }
    public void setPages(int Pages){
        this.Pages = Pages;
    }
    public String getAuthor(){
        return Author;
    }
    public void setAuthor(String Author){
        this.Author = Author;
    }

    public String toString(){
        return "Код источника - "+SourceCode+"\n"+"Тип литературы - "+TypeLiterature+"\n"+"Название - "+Name+"\n"+"Год издательства - "+YearPublishing+"\n"+"Название издательства - "+NamePublishing+"\n"+"Количество страниц - "+Pages+"\n"+"Автор - "+Author;
    }
}