/**
 * Sudoku Solution Validator by Stilian Balasopoulov
 * CS3600(a)
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <pthread.h>
#define NUM_THREADS 27
#define pass (void) 0

int valid[NUM_THREADS] = {0};
int sudoku[9][9];
int numPuzzle = 1;

typedef struct {
	int row;
	int column;
} parameters;

// Checks if 3x3 grid in sudoku[][] contains only numbers 1-9
void *gridValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i, j;

	// Verifying parameters conform to 3x3 grid
	if (row > 6 || row % 3 != 0 || col > 6 || col % 3 != 0) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number contains only numbers 1-9
	for (i = row; i < row + 3; i++) {
		for (j = col; j < col + 3; j++) {
			int num = sudoku[i][j];
			if (num < 1 || num > 9 || validArray[num - 1] == 1)
				pthread_exit(NULL);
			else validArray[num - 1] = 1;
		}
	}
	// Inputs validation into boolean array
	valid[row + col / 3] = 1;
	pthread_exit(NULL);
}

// Checks if column contains only numbers 1-9
void *columnValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i;

	// Verifying parameters conform to a column
	if (row != 0 || col > 8) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number in column is between 1-9
	for (i = 0; i < 9; i++) {
		int num = sudoku[i][col];
		if (num < 1 || num > 9 || validArray[num - 1] == 1)
			pthread_exit(NULL);
		else validArray[num - 1] = 1;
	}

	// Inputs validation into boolean array
	valid[18 + col] = 1;
	pthread_exit(NULL);
}

// Checks if row contains only numbers 1-9
void *rowValid (void* param) {
	parameters *params = (parameters *) param;
	int row = params->row;
	int col = params->column;
	int validArray[9] = {0}, i;

	// Verifying parameters conform to a column
	if (col != 0 || row > 8) {
		printf("Invalid row or column. row = %d col = %d", row, col);
		pthread_exit(NULL);
	}

	// Verifying each number in row is between 1-9
	for (i = 0; i < 9; i++) {
		int num = sudoku[row][i];
		if (num < 1 || num > 9 || validArray[num - 1] == 1)
			pthread_exit(NULL);
		else validArray[num - 1] = 1;
	}

	// Inputs validation into boolean array
	valid[9 + row] = 1;
	pthread_exit(NULL);
}

int validateSudokuPuzzle(FILE *inputFile, FILE *outputFile) {
	pthread_t threads[NUM_THREADS];
	int threadsIndex = 0;
	int i,j;

	// Scanning input file and placing numbers in puzzle
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			char c;
			if (fscanf(inputFile, " %c", &c) != 1)
				pass;
			else if (isdigit((unsigned char)c))
				sudoku[i][j] = c - '0';
		}
	}

	// Printing Sudoku Puzzle to testResults.txt
	fprintf(outputFile, "Sudoku Puzzle #%d\n", numPuzzle);
	numPuzzle++;
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			fprintf(outputFile, "%d ", sudoku[i][j]);
		}
		fprintf(outputFile, "\n");
	}

	// Run each function based on the location of data given (column, row, or 3x3 grid)
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			if (i % 3 == 0 && j % 3 == 0) {
				parameters *data = (parameters *) malloc(sizeof(parameters));
				data->row = i;
				data->column = j;
				pthread_create(&threads[threadsIndex++], NULL, gridValid, data);
			}
			if (i == 0) {
				parameters *colData = (parameters *) malloc(sizeof(parameters));
				colData->row = i;
				colData->column = j;
				pthread_create(&threads[threadsIndex++], NULL, columnValid, colData);
			}
			if (j == 0) {
				parameters *rowData = (parameters *) malloc(sizeof(parameters));
				rowData->row = i;
				rowData->column = j;
				pthread_create(&threads[threadsIndex++], NULL, rowValid, rowData);
			}
		}
	}

	// Wait for all threads to finish.
	for (i = 0; i < NUM_THREADS; i++) {
		pthread_join(threads[i], NULL);
	}

	// If valid contains a 0, then the solution is invalid.
	for (i = 0; i < NUM_THREADS; i++) {
		if (valid[i] == 0) {
			fprintf(outputFile, "Solution is Invalid.\n\n");
			return 0;
		}
		// Clearing valid[] array for next solution.
		valid[i] = 0;
	}

	fprintf(outputFile, "Solution is Valid!\n\n");
	return 0;
}

int main() {
	int i,j;

	// Initializing all sudoku testing files.
	FILE *sudokuPuzzle1 = fopen("SudokuPuzzle1.txt", "r");
	FILE *sudokuPuzzle2 = fopen("SudokuPuzzle2.txt", "r");
	FILE *sudokuPuzzle3 = fopen("SudokuPuzzle3.txt", "r");
	FILE *testResults = fopen("testResults.txt", "w");

	// Validating that each puzzle has an input.
	if (sudokuPuzzle1 == NULL || sudokuPuzzle2 == NULL || sudokuPuzzle3 == NULL || testResults == NULL) {
		printf("ERROR: Could not open txt file.");
		exit(-1);
	}

	// Testing each puzzle from each file.
	validateSudokuPuzzle(sudokuPuzzle1, testResults);
	validateSudokuPuzzle(sudokuPuzzle2, testResults);
	validateSudokuPuzzle(sudokuPuzzle3, testResults);

	return 0;
}
