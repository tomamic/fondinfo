//This is the file discountsale.h.
//This is the interface for the class DiscountSale.

#ifndef DISCOUNTSALE_H
#define DISCOUNTSALE_H
#include "sale.h"

namespace SavitchSale
{

    class DiscountSale : public Sale
    {

    public:
        DiscountSale( );
        DiscountSale(double thePrice, double theDiscount);
        //Discount is expressed as a percent of the price.
        //A negative discount is a price increase.
        double getDiscount( ) const;
        void setDiscount(double newDiscount);
        double bill( ) const;
    private:
        double discount;

    };

}//SavitchSale

#endif //DISCOUNTSALE_H
