#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <string.h>

// GSL library
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>

//#include "solve_tridiag.h"

using namespace std;

double GaussianRBF(vector<double> x, vector<double> y, vector<double> z, double sigma_x, double sigma_y,
	vector<double> const & x_vis,
    vector<double> const & y_vis,
    // output
    vector<double> & z_vis){

    int N=x.size();
	vector<double> A(N*N,0);

  	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){

			//G[n*i+j]=(1/2*3.14*sigmax*sigmay)*exp((-1/2)*(pow((x[i]-x[j]),2)/pow(sigmax,2)+ pow((y[i]-y[j]),2) /pow(sigmay,2)));
			A[N*i+j]=gsl_ran_gaussian_pdf((x[i]-x[j]),0.8)*gsl_ran_gaussian_pdf((y[i]-y[j]),0.8);
		}
	}

	gsl_matrix * A_gsl = gsl_matrix_alloc(N,N);
	gsl_vector * z_gsl = gsl_vector_alloc(N);

	for (int i = 0; i < N; i++)
    	for (int j = 0; j < N; j++)
      		gsl_matrix_set(A_gsl, i, j, A[N*i+j]);

	for (int i = 0; i < N; i++)
		gsl_vector_set(z_gsl,i, z[i]);

	gsl_permutation * p_gsl = gsl_permutation_alloc(N);
	int signum; 


    gsl_linalg_LU_decomp(A_gsl, p_gsl, &signum);

    gsl_vector * d_gsl = gsl_vector_alloc(N);
    gsl_linalg_LU_solve(A_gsl, p_gsl, z_gsl, d_gsl);

    vector<double> d(N,0);
    for (int i = 0; i < N; i++)
		d[i]=gsl_vector_get(d_gsl,i);

	// Evaluate the interpolation function on the visualisation grid (x_vis,y_vis,z_vis).
    // Remember that z_vis[i*N_vis+j]=f(x_vis[i],y_vis[j])
    int N_vis_x = x_vis.size();
    int N_vis_y = y_vis.size();
    for(int i=0; i<N_vis_x; ++i)
        for(int j=0; j<N_vis_y; ++j)
            {
                double t = 0;
                // loop over all the data points
                for(int k=0; k<N; ++k)
                    t += d[k]*gsl_ran_gaussian_pdf(x_vis[i]-x[k],sigma_x)*
                        gsl_ran_gaussian_pdf(y_vis[j]-y[k],sigma_y);

                z_vis[i*N_vis_y+j] = t;
            }

    gsl_matrix_free(A_gsl);
    gsl_vector_free(z_gsl);
    gsl_permutation_free(p_gsl);
    gsl_vector_free(d_gsl);
  
/*

	// Solve the system Ad = z, store the result in a vector d
    gsl_matrix * A_gsl = gsl_matrix_alloc(N,N);
    memcpy(A_gsl->data, &A[0], N*N*sizeof(double));
    gsl_vector * z_gsl = gsl_vector_alloc(N);
    memcpy(z_gsl->data, &z[0], N*sizeof(double));

    gsl_permutation * p_gsl = gsl_permutation_alloc(N);
    int signum;
    gsl_linalg_LU_decomp(A_gsl, p_gsl, &signum);

    gsl_vector * d_gsl = gsl_vector_alloc(N);
    gsl_linalg_LU_solve(A_gsl, p_gsl, z_gsl, d_gsl);

    vector<double> d(N,0);
    memcpy(&d[0], d_gsl->data, N*sizeof(double));

*/

    

}

int main(int argc, char const *argv[])
{
	/* code */
    // pass the file name to read the data from as a command line argument argv[1]
    if(argc != 3)
    {
        cout << "Usage: " << argv[0] << " <sigma_x> <sigma_y>" << endl;
        return -1;
    }

	vector<double> x;
	vector<double> y;
	vector<double> z;
    // read the data points (x_i,y_i,z_i)
    ifstream infile;
    infile.open("q2-data.txt");

    double xi, yi, zi;
    while(infile >> xi >> yi >> zi)
    {
        x.push_back(xi);
        y.push_back(yi);
        z.push_back(zi);
    }

    if(x.empty() || y.empty() || z.empty())
    {
        cout << "No data read from file q2-data.txt, stop." << endl;
        return -1;
    }
    cout << "(q2.cpp) Got " << x.size() << " points from q2-data.txt\n";

    // compute the interpolation function f and store the (x,y,f(x,y)) 
    // values on a fine mesh
    int N_vis_x = 100;
    int N_vis_y = 100;
    vector<double> x_vis(N_vis_x,0);
    vector<double> y_vis(N_vis_y,0);
    // z[i*N_vis_y+j] = f(x[i],y[j])
    vector<double> z_vis(N_vis_x*N_vis_y,0);

    // visualisation nodes for x
    double min_x = *min_element(x.begin(), x.end());
    double max_x = *max_element(x.begin(), x.end());
    double h_x = (max_x-min_x)/(N_vis_x-1);
    for(int i=0; i<x_vis.size(); ++i)
        x_vis[i] = min_x + i*h_x;

    // visualisation nodes for y
    double min_y = *min_element(y.begin(), y.end());
    double max_y = *max_element(y.begin(), y.end());
    double h_y = (max_y-min_y)/(N_vis_y-1);
    for(int i=0; i<y_vis.size(); ++i)
        y_vis[i] = min_y + i*h_y;

    double sigma_x = atof(argv[1]);
    double sigma_y = atof(argv[2]);

    GaussianRBF(x, y, z, sigma_x, sigma_y,x_vis,y_vis,z_vis);

    // write data to the output file
    ofstream outfile;
    cout << "(q2.cpp) Writing " << N_vis_x*N_vis_y << " points to q2-result.txt\n";
    outfile.open("q2-result.txt");
    for(int i=0; i<N_vis_x; ++i)
        for(int j=0; j<N_vis_y; ++j)
            outfile << x_vis[i] << " " << y_vis[j] << " " << z_vis[i*N_vis_y+j] << endl;


/*
  double a_data[] = { 0.18, 0.60, 0.57, 0.96,
                      0.41, 0.24, 0.99, 0.58,
                      0.14, 0.30, 0.97, 0.66,
                      0.51, 0.13, 0.19, 0.85 };

  double b_data[] = { 1.0, 2.0, 3.0, 4.0 };

  gsl_matrix_view m
    = gsl_matrix_view_array(a_data, 4, 4);

  gsl_vector_view b
    = gsl_vector_view_array(b_data, 4);

  gsl_vector *xx = gsl_vector_alloc(4);

  int s;

  gsl_permutation * p = gsl_permutation_alloc(4);

  gsl_linalg_LU_decomp(&m.matrix, p, &s);

  gsl_linalg_LU_solve(&m.matrix, p, &b.vector, xx);

  printf ("xx = \n");
  gsl_vector_fprintf(stdout, xx, "%g");

  gsl_permutation_free(p);
  gsl_vector_free(xx);
*/

	return 0;
}