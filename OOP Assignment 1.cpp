#include<iostream>
using namespace std;
class complex
{
    float real,img;
    public:
    complex()
    {
        real=0;
        img=0;
    }
    complex operator +(complex const &obj)
    {
        complex temp;
        temp.real=real+obj.real;
        temp.img=img+obj.img;
        return (temp);
    }
    complex operator *(complex const &obj)
    {
        complex temp;
        temp.real=(real*obj.real)-(img*obj.img);
        temp.img=(real*obj.img)+(img*obj.real);
        return (temp);
    }
    friend ostream &operator<<(ostream&,complex&);
    friend istream &operator>>(istream&,complex&);
};

ostream &operator<<(ostream& output,complex& obj)
{
    output<<obj.real;
    output<<"+"<<obj.img<<"i";
    return output;
}

istream &operator>>(istream& input,complex& obj)
{
    cout<<"Enter real part:";
    input>>obj.real;
    cout<<"Enter imaginary part:";
    input>>obj.img;
    return input;
}


int main()
{
    complex a,b,c,d;
    cout<<"For First Complex Number"<<endl;
    cin>>a;

    cout<<"\nFor Second Complex Number"<<endl;
    cin>>b;

    cout<<"\n****Arithmetic Operations**** "<<endl;
    c=a+b;
    cout<<"\n Addition is: "<<c<<endl;

    d=a*b;
    cout<<"\n Multiplication is: "<<d<<"\n";
    return 0;
}
