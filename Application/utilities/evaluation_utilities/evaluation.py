import multiprocessing
import subprocess
import utilities
def run_python_file(filename):
    """Runs the specified Python file and returns its output."""
    try:
        process = subprocess.Popen(['python', filename], stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    except:
        None
    output, _ = process.communicate()
    return output.decode('utf-8')
def evaluation_answer(candida):
    # List of Python files to execute
    filenames = ['solution.py']

    candidate=candida
    for emai in candidate:
        name=emai.split('@')[0]
        name+=".py"
        filenames.append(name)
    filepath="downloaded_answer/"
    for i in range(len(filenames)):
        filenames[i]=filepath+filenames[i]
    # Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Run each Python file in a separate process and get its output
    try:
        results = [pool.apply_async(run_python_file, args=(filename,)) for filename in filenames]
        outputs = [result.get() for result in results]
    except:
        None
    solution_output=None
    # Print the output of each Python file
    for filename, output in zip(filenames, outputs):
        filename=filename.split("/")[1]
        if filename=="solution.py":
            solution_output=output
    for filename, output in zip(filenames, outputs):
        filename=filename.split("/")[1]
        filename=filename.split(".py")[0]
        for item in candidate:
            if filename in item:
                filename=item
        #print(f"Output of {filename}:")
        #print(output)
        client=utilities.mongo_local()
        db=client.hushHush
        collection = db.Email
        if output==solution_output and filename!="solution":
            mongo_data={"recipient":filename,"solution":True}
            filtering={"recipient":filename}
            utilities.mongoimportupdate(mongo_data,filtering,"hushHush","Email")
            print(f"Candidate with the Email address: {filename}, successfully answer the question")
        elif output!=solution_output and output!=None and output!="" and len(output)!=0:
            mongo_data={"recipient":filename,"solution":False}
            filtering={"recipient":filename}
            utilities.mongoimportupdate(mongo_data,filtering,"hushHush","Email")
            print(f"Unfortunately,Candidate with the Email address: {filename}, was wrong")
    return output
        

