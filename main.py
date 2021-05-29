class BankAccount:
    def __init__(self,acou,passw,inibal,W_Amount,d_amount,w_answ,d_ans,j_answr,di_answer,d_psw,d_password,de_p,w_password ):
        self.acc  = acou
        self.passw = passw
        self.inibal = inibal
        self.W_Amount = W_Amount
        self.amount = d_amount
        self.w_answ = w_answ
        self.d_ans = d_ans
        self.j_answr = j_answr
        self.di_answer = di_answer
        self.d_psw = d_psw
        self.d_password = d_password
        self.de_p = de_p
        self.w_password =w_password

    def input_att(self):
        self.acc = input("Faka inombolo yokwenza akhawunti")
        self.passw = input("Yenza inombolo ozovula ngayo iAkhawunti yakho")
        self.inibal = float(input("Faka imali yokuqala kwi akhawunti yakho"))

    def confirm_pass(self):
        pword = input("Phinda ufake le nombolo yokuvula ubuyifakile")
        while pword != self.passw:
            pword = input("Faka inombolo yokuvula efana nale yokuqala")
        print("Ukwazile ukwenza iAkhawunti ebhankini yethu siyabulela")


    def Deposit(self):
        self.d_ans = input("Uyafuna na ukufaka imali kwi akhawunti yakho?")
        if self.d_ans == "ewe" or self.d_ans == "Ewe" or self.d_ans == "EWE":
            self.j_answr = input("Yiyo na le akhawunti ufuna ukuyithumelela le: " + self.acc)
            if self.j_answr == "ewe" or self.j_answr == "Ewe" or self.j_answr == "EWE":
                self.d_amount = float(input(" Bhala lemali ufuna ukuyifaka kwi akhawunti yakho"))
                self.d_password = input("Faka inombolo echanekileyo yokuvula")
                while self.d_password != self.passw:
                    self.d_password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
                print("Yinombolo echanekileyo le")
                print("Ingenile imali ekuyi R ", self.d_amount, " kwi akhawunti engu ", self.acc)
                current = self.inibal + self.d_amount
                return current
            elif self.j_answr == "hayi" or self.j_answr == "Hayi" or self.j_answr == "HAYI":
                acc_n = input("Faka inombolo ye akhawunti yakho elungileyo")
                self.d_amount = float(input(" Bhala lemali ufuna ukuyifaka kwi akhawunti yakho"))
                self.d_password = input("Faka inombolo echanekileyo yokuvula")
                while self.d_password != self.passw:
                    self.d_password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
                print("Yinombolo echanekileyo le")
                print("Ingenile imali ekuyi R ", self.d_amount, " kwi akhawunti engu ", self.acc)
                current = self.inibal + self.d_amount
                return current
        elif self.d_ans == "hayi" or self.d_ans == "Hayi" or self.d_ans == "HAYI":
            current = self.inibal
            return current


    def Withdraw(self,c):
        self.w_answ = input("Uyafuna ukukhupha imali?")
        if self.w_answ == "ewe" or self.w_answ == "Ewe" or self.w_answ == "EWE":
            self.W_Amount = float(input(" Faka imali ofuna ukuyikhupha"))
            w_password = input("Faka inombolo echanekileyo yokuvula")
            while self.w_password != self.passw:
                self.w_password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
            print("Yinombolo echanekileyo le")
            print("Ukhuphe imali engange R ", self.W_Amount, "kwi akhawunti yakho")
            C_bal = c - self.W_Amount
            return C_bal
        elif self.w_answ == "hayi" or self.w_answ == "Hayi" or self.w_answ == "HAYI":
            C_bal = c
            return C_bal

    def Display(self,c):
        self.di_answer = input("Uyafuna na ukubona imali eshiyekileyo kwi akhawunti yakho")
        if self.di_answer == "ewe" or self.di_answer == "Ewe" or self.di_answer == "EWE":
            d_psw = input("Faka inombolo yokuvula echanekileyo")
            while d_psw != self.passw:
                d_psw = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
            print("Yinombolo echanekileyo le")
            print(" Imali eshiyekileyo kwi akhawunti yakho yebhanki yi : R", c)
        elif self.di_answer == "hayi" or self.di_answer == "Hayi" or self.di_answer == "HAYI":
              print("Ugqibile ukusebenzisa ibhanki okwangoku")
        print("Siyabulela ngokuba usebenzise lebhanki yethu")

class Main:
    if __name__ == '__main__':
        obj2 = BankAccount("","",0,0,0,"","","","","","","","")
        obj2.input_att()
        obj2.confirm_pass()
        c_bal = obj2.Deposit()
        cure_bal = obj2.Withdraw(c_bal)
        obj2.Display(cure_bal)
