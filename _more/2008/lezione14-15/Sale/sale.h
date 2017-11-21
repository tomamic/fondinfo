//This is the header file sale.h. 
//This is the interface for the class Sale.
//Sale is a class for simple sales.

#ifndef SALE_H
#define SALE_H


namespace SavitchSale
{

    class Sale
    {
    public:
        Sale( );
        Sale(double thePrice);
        double getPrice( ) const;
        void setPrice(double newPrice);
        virtual double bill( ) const;
        double savings(const Sale& other) const;
        //Returns the savings if you buy other instead of the calling object.
    private:
        double price;
    };

    bool operator < (const Sale& first, const Sale& second);
    //Compares two sales to see which is larger.

}//SavitchSale

#endif // SALE_H
