#public class SerVivo {
#    Date data_nascimento;
#    public SerVivo (Date data_nascimento) {
#        this.data_nascimento = data_nascimento;
#    }
#}
class SerVivo :
    def __init__ (self, data_nascimento):
        self.__data_nascimento = data_nascimento

#public class Cachorro extends SerVivo{
class Cachorro (SerVivo) :
#    private String nome;
#    private String raca;
#    public Cachorro(Date data_nascimento, String nome, String raca) {
#        super(data_nascimento);
#        this.nome = nome;
#        this.raca = raca;
#    }
    def __init__ (self, data_nascimento, nome, raca):
        super().__init__ (data_nascimento)
        self.__nome = nome
        self.__raca = raca
#    public String getNome() {
#        return nome;
#    }
    def getNome (self) :
        return self.__nome
#    public void setNome(String nome) {
#        this.nome = nome;
#    }
#    public String getraca() {
#        return raca;
#    }
#    public void setraca(String raca) {
#        this.raca = raca;
#    }
#    public String toString () {
#        String str =
#                "Cachorro: " + this.nome + "\n"
#            +   "raca: " + this.raca;
#        ;
#        return str;
#    }
#    public static void main (String [] args) {
#        Cachorro c = new Cachorro (new Date (), "Shurastey", "Golden Retriever");
#        System.out.println (c.toString());
#    }
#}
