#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <string.h>

using namespace std;

int main(int argc, char const *argv[])
{
	//Given data values
	double re=0.095;
	double r0=0.145;
	double theta_p=0.7015;
	double num;
	double den;
	
	    // storage for the interpolation nodes
    vector<double> x;
    vector<double> y;
    

    // read the data points 
    ifstream infile;
    infile.open("input_values.txt");

    double xi, yi;
    while(infile >> xi >> yi)
    {
        x.push_back(xi);
        y.push_back(yi);

    }
    double s=0;
    double ss=0;
	int N=x.size()-1;

	for(int i=0; i<N; ++i){

		s=s+(x[i+1]-x[i])*(theta_p*x[i]*y[i]+theta_p*x[i+1]*y[i+1])/2;
		ss=ss+(x[i+1]-x[i])*(theta_p*x[i]+theta_p*x[i+1])/2;
	}

    cout<<s/ss<<endl;
    /*Answer will be 567.91*/
	return 0;
}