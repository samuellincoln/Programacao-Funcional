import datetime
from abc import ABC, abstractmethod
class Locomocao (ABC):
    @abstractmethod
    def virevolante (self) :
        pass
    @abstractmethod
    def freie (self) :
        pass
    @abstractmethod
    def acelere (self) :
        pass
    @abstractmethod
    def pise_na_embreagem (self) :
        pass
class Carro (Locomocao) :
    def __init__ (self, marca, ano) :
        self.__marca = marca
        self.__ano = ano
    def toString (self) :
        return "Carro (" + self.__marca + ", " + self.__ano + ")"
    def virevolante (self) :
        print ("Volante virado")
    def freie (self) :
        print ("Freou carro")
    def acelere (self) :
        print ("Acelerou carro")
    def pise_na_embreagem (self) :
        print ("Pisou na embreagem")


c = (Carro ("Honda", "2023"))
print (c.toString())

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
    def setNome (self, nome):
        self.__nome = nome
#    public String getraca() {
#        return raca;
#    }
    def getRaca (self):
        return self.__raca
#    public void setraca(String raca) {
#        this.raca = raca;
#    }
    def setRaca (self, raca):
        self.__raca = raca
#    public String toString () {
#        String str =
#                "Cachorro: " + this.nome + "\n"
#            +   "raca: " + this.raca;
#        ;
#        return str;
#    }
    def toString (self) :
        var_str = "Cachorro: " + self.__nome + "\n" + "Raca: " + self.__raca
        return var_str
#    public static void main (String [] args) {
#        Cachorro c = new Cachorro (new Date (), "Shurastey", "Golden Retriever");
#        System.out.println (c.toString());
#    }
c = Cachorro (datetime.datetime.now(), "Shurastey", "Golden Retriever")
print (c.toString())
#}
