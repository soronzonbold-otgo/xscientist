#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <string.h>

#include "3x3_matrix_inv.h"
using namespace std;

void Jacobian(vector<double> &k,vector<double> &J){

	J[0]=exp(k[1]*0.1);
	J[1]=k[0]*0.1*exp(k[1]*0.1);
	J[2]=0.1;

	J[3]=exp(k[1]*0.2);
	J[4]=k[0]*0.2*exp(k[1]*0.2);
	J[5]=0.2;

	J[6]=exp(k[1]*0.3);
	J[7]=k[0]*0.3*exp(k[1]*0.3);
	J[8]=0.3;

}



void system_fnc(vector<double> &J,vector<double> &k,vector<double> &y){

	vector<double> Jac(9);
	vector<double> f(3);
	invert_3x3_matrix(J,Jac);

	f[0]=k[0]*exp(k[1]*0.1)+k[2]*0.1-100;
	f[1]=k[0]*exp(k[1]*0.2)+k[2]*0.2-120;
	f[2]=k[0]*exp(k[1]*0.3)+k[2]*0.3-150;

	y[0]=-(Jac[0]*f[0]+Jac[1]*f[1]+Jac[2]*f[2]);
	y[1]=-(Jac[3]*f[0]+Jac[4]*f[1]+Jac[5]*f[2]);
	y[2]=-(Jac[6]*f[0]+Jac[7]*f[1]+Jac[8]*f[2]);
	
}

void update_solution( vector<double> & x_curr, vector<double> & x_prev, vector<double> & y )
{
    for( unsigned i = 0; i < x_curr.size(); ++i ) {

        x_curr[i] = x_prev[i] + y[i];
        
    }
}

int main()
{
	
	vector<double> calc_J(9);
	vector<double> calc_y(3);

	vector<double> x_prev(3);
	vector<double> x_curr(3);
	const unsigned Nmax=20;
	const double tol = 1.e-5; 

	x_curr[0]=80;
	x_curr[1]=10;
	x_curr[2]=20;



	int N=0;
	
	while(N<=Nmax){
		x_prev=x_curr;

		Jacobian(x_prev,calc_J);
		system_fnc(calc_J,x_prev,calc_y);
		update_solution( x_curr, x_prev, calc_y);
		cout<<x_curr[0]<<' '<<x_curr[1]<<' '<<x_curr[2]<<endl;

		if(sqrt(pow(calc_y[0],2)+pow(calc_y[1],2)+pow(calc_y[2],2))<tol){
						break;
		}
		++N;

	}
	

	return 0;
}
//БОДЛОГЫН ГАРАЛТ ШИЙД

/*
k1     	   k2		k3
284.579 1.49448 -4886.02
88.2016 2.04923 -207.507
87.8416 2.71896 -150.7
87.7198 2.60182 -137.774
87.7129 2.59696 -137.229
87.7129 2.59695 -137.228
87.7129 2.59695 -137.228
*/