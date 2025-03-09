import os 
import ttkbootstrap as ttk 
import inspect 
from tkinter import filedialog 

def select_files():
    root = ttk.Window() 
    root.withdraw()  # Hide the root window

    file_paths = filedialog.askopenfilenames(title="Select File(s)")  # Open file picker

    return file_paths  # Returns a tuple of selected file paths 


def listSubPaths(dirPath): 
    subPaths = [] 
    for subPath in os.listdir(dirPath): 
        absPath = os.path.join(dirPath,subPath) 
        absPath = absPath.replace("\\","//") 
        subPaths.append(absPath) 
        if os.path.isdir(absPath): 
            subPaths.extend(listSubPaths(absPath)) 
    return subPaths 

def countmatches(seq1, seq2): 
    score = 0 
    for char1, char2 in zip(seq1, seq2): 
        if char1 == char2: 
            score += 1 
    return score 

def sortFiles(sortDirPath): 
    subPaths = listSubPaths(sortDirPath) 
    for path in subPaths: 
        if not os.path.isdir(path): 
            pathParts = path.split("\\") 
            nameParts = pathParts[-1+len(pathParts)].split(".") 
            fileType = nameParts[-1+len(nameParts)] 
            outputDir = os.path.join(sortDirPath,fileType) 
            os.mkdir(outputDir) if not os.path.isdir(outputDir) else None 
            fileName = "" 
            for part in nameParts[0:-1+len(nameParts)]: 
                fileName += part 
            index = "" 
            outputPath = os.path.join(outputDir,f"{fileName}{index}.{fileType}") 
            if os.path.exists(outputPath): 
                index = 0 
                while os.path.exists(outputPath): 
                    index += 1 
                    outputPath = os.path.join(outputDir,f"{fileName}{index}{fileType}") 
            os.rename(path,outputPath) 


def pyckage(targetPath="", pyckageName="pyckaged", destinationPath=""): 
    
    if destinationPath == "": 
        destinationPath = targetPath 

    targetPathStandardised = targetPath.replace("\\","//") 

    fileData = {} 
    unpackagedPaths = [] 
    installerFileData = ["import os \n"] 

    subPaths = listSubPaths(targetPath) 
    for path in subPaths: 
        if not(os.path.isdir(path)): 
            try: 
                file = open(path, encoding="UTF-8",mode="r") 
                data = str(file.readlines() ) 
                if data != []: 
                    fileData[path] = data 
                file.close() 
                installerFileData.append(f"file_instance = open(__file__.removesuffix('{pyckageName}.py')+'{path.removeprefix(targetPathStandardised)}','w') \n") 
                installerFileData.append(f"file_instance.writelines({fileData[path]}) \n") 
                installerFileData.append(f"file_instance.close() \n") 
            except: 
                print(f"Could not package: {path.removeprefix(targetPathStandardised)}") 
                unpackagedPaths.append(path) 
        else: 
            installerFileData.append(f"os.mkdir(__file__.removesuffix('{pyckageName}.py')+'{path.removeprefix(targetPathStandardised)}') \n") 

    installerFile = open(os.path.join(destinationPath,f"{pyckageName}.py"),"w") 
    installerFile.writelines(installerFileData) 
    installerFile.close() 
def select_from_list(options):
    """Creates a pop-up window with a Treeview and returns the selected option."""
    def on_select():
        """Gets the selected item and closes the window."""
        nonlocal selected_option
        selected_item = listbox.selection()  # Get selected item ID
        if selected_item:
            selected_option = listbox.item(selected_item[0], "values")[0]  # Extract value
            root.destroy()  # Close the pop-up window

    # Create the pop-up window
    root = ttk.Window()
    root.title("Select an Option")
    root.geometry("300x250")

    # Create a frame to hold treeview and scrollbar
    frame = ttk.Frame(root)
    frame.pack(pady=10, fill=ttk.BOTH, expand=True)

    # Create a Treeview with a single column
    listbox = ttk.Treeview(frame, columns=("Option",), show="headings", height=5)
    listbox.heading("Option", text="Options")  # Set column heading
    listbox.column("Option", width=250, anchor="center")  # Adjust column width

    # Create and link scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=ttk.VERTICAL, command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)

    # Pack treeview and scrollbar
    listbox.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=True)
    scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)

    # Insert options into the treeview
    for option in options:
        listbox.insert("", "end", values=(option,))

    # Button to confirm selection
    button = ttk.Button(root, text="Select", command=on_select)
    button.pack(pady=10)

    # Variable to store selection
    selected_option = None

    # Run the pop-up and wait for selection
    root.mainloop()

    return selected_option  # Return the selected option

# Example Usage:
# choice = select_from_list(["Apple", "Banana", "Cherry"])
# print(f"Selected: {choice}")

# Example Usage:
# choice = select_from_list(["Apple", "Banana", "Cherry"])
# print(f"Selected: {choice}")

def getFunctions(module): 
    output = {} 
    functions = inspect.getmembers(module, inspect.isfunction) 
    for functionName, functionLocation in functions: 
        output[functionName] = functionLocation 
    return output 

def getClasses(module): 
    output = {} 
    classes = inspect.getmembers(module, inspect.isclass) 
    for className, classLocation in classes: 
        output[className] = classLocation 
    return output 

def extract_frames(video_path, output_folder_path):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame as image
        frame_filename = os.path.join(output_folder_path, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    # Release video capture
    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder_path}") 

def spacestringrecursion(input_string, output, current_depth, max_depth, filler_chr): 
    if current_depth < max_depth: 
        for i in range(0,len(input_string)+1): 
            spaced_instance = input_string[0:i] + filler_chr + input_string[i:] 
            if spaced_instance not in output.keys(): 
                spacestringrecursion(spaced_instance, output, current_depth+1, max_depth, filler_chr) 
    else: 
        output[input_string] = "" 
    return output 

def multispacestring(input_string, depth, filler_chr=" "): 
    output = spacestringrecursion(input_string, {}, 0, depth, filler_chr) 
    return output 

def alignStrings(modseq, refseq): 
    refseq = "".ljust(len(modseq), " ") + refseq + "".ljust(len(modseq), " ") 
    alignment_index = -len(modseq) 
    modseq = modseq.ljust(len(refseq), " ") 
    max_score = 0 
    for i in range(0,len(refseq)): 
        modseq_instance = "".ljust(i, " ") + modseq[0:-i+len(modseq)] 
        score = countmatches(modseq_instance, refseq) 
        if max_score < score: 
            max_score = score 
            alignment_index = i 
    return alignment_index 

def sortbylength(seqs): 
    sort_dict = {} 
    for i in seqs: 
        if len(i) in sort_dict.keys() : 
            sort_dict[len(i)].append(i) 
        else : 
            sort_dict[len(i)] = [i] 
    
    output = [] 
    for i in sorted(list(sort_dict.keys())): 
        output.extend(sort_dict[i]) 
    return output 

def findalignment(modseq_aligned, refseq, filler_chr=" "): # returns the alignment offset and a score. Filler_chr must be a character that does not occur in the inputs 
    
    scores = {}
    shift = 0
    alignment = 0
    original_refseq = refseq[0:] 
    forwardpaddedrefseq = refseq + filler_chr*len(refseq) 
    refseq = filler_chr*len(refseq) + refseq + filler_chr*len(refseq) 
    alignment_padding = (-len(modseq_aligned)+len(refseq)) 
    modseq_aligned += filler_chr*alignment_padding 
    highest_score = 0 

    for position in range(0,len(forwardpaddedrefseq)):
        score = countmatches(modseq_aligned, refseq)
        if highest_score < score:
            highest_score = score
            alignment = shift 
        modseq_aligned = filler_chr + modseq_aligned[0:-1+len(modseq_aligned)]
        shift += 1 

    return alignment-len(original_refseq), highest_score-2*len(original_refseq) 

def countmatches(modseq_aligned, refseq): # counts number of matches between 2 strings or equal length 
    score = 0 
    for index in range(0,len(refseq)) : 
        if modseq_aligned[index] == refseq[index]:
            score += 1 
        else: 
            pass
    return score 

def spacestringrecursion(input_string, outputs, current_depth, max_depth, filler_chr): 
    if current_depth < max_depth: 
        for i in range(0,len(input_string)+1): 
            spaced_instance = input_string[0:i] + filler_chr + input_string[i:] 
            if spaced_instance not in outputs.keys(): 
                spacestringrecursion(spaced_instance, outputs, current_depth+1, max_depth, filler_chr) 
    else: 
        outputs[input_string] = "" 
    return outputs 

def multispacestring(input_string, depth, filler_chr=" "): 
    ''' 
    "hiii" 
    → "  hiii" 
    → " h iii" 
    → " hi ii" 
    → " h iii" 
    → "h iii " 
    → "h ii i" 
    → "h i ii" 
    → "h  iii" 
    → "hi ii " 
    → "hi ii " 
    → "hi i i" 
    → "hi  ii" 
    → "hii i " 
    → "hii  i" 
    → "hiii  " 

    The space moves. The depth refers to the number of spaces. The filler_chr is the space in this example. Must be a character that does not occur in any of the inputs. 
    ''' 
    outputs = spacestringrecursion(input_string, {}, 0, depth, filler_chr) 
    outputs = list(outputs.keys() ) 
    return outputs 

def sortbylength(seqs): # sorts a list of itterables by their lengths 
    sort_dict = {} 
    for i in seqs: 
        if len(i) in sort_dict.keys() : 
            sort_dict[len(i)].append(i) 
        else : 
            sort_dict[len(i)] = [i] 
    
    output = [] 
    for i in sorted(list(sort_dict.keys())): 
        output.extend(sort_dict[i]) 
    return output 

def levenshtein_distance(seq1, seq2, filler_chr=" "): 
    modseq, refseq = sortbylength([seq1, seq2]) 

    if not(len(modseq) == len(refseq)): 

        alignment, score = findalignment(modseq, refseq, filler_chr) 

        if alignment < 0: 
            refseq = "".ljust(abs(alignment), " ") + refseq 
        else: 
            modseq = "".ljust(alignment, " ") + modseq 

        max_score = 0 
        seqlen_difference = len(refseq)-len(modseq) 
        for i in multispacestring(modseq,seqlen_difference, filler_chr): 
            score = countmatches(i, refseq) 
            if max_score <= score: 
                max_score = score 
                modseq = i 
    else: 

        parts = [] 

        mode = modseq[0] == refseq[0] 

        modpart = "" 
        refpart = "" 

        for modchr, refchr in zip(modseq, refseq): 
            if mode: 
                if modchr == refchr: 
                    modpart += modchr 
                    refpart += refchr 
                else: 
                    parts.append([modpart, refpart]) 
                    modpart = modchr 
                    refpart = refchr 
                    mode = False 
            else: 
                if modchr != refchr: 
                    modpart += modchr 
                    refpart += refchr 
                else: 
                    parts.append([modpart, refpart]) 
                    modpart = modchr 
                    refpart = refchr 
                    mode = True 
        parts.append([modpart, refpart]) 

        modseq = "" 
        refseq = "" 

        for pair in parts: 
            if pair[0] != pair[1]: 
                alignment, score = findalignment(pair[0], pair[1], filler_chr) 
                if alignment < 0: 
                    refseq_part = "".ljust(abs(alignment), " ") + pair[1] 
                    refseq += refseq_part 
                    modseq += pair[0].ljust(len(refseq_part), " ") 
                elif 0 < alignment: 
                    modseq_part = "".ljust(alignment, " ") + pair[0] 
                    modseq += modseq_part 
                    refseq += pair[1].ljust(len(modseq_part), " ") 
            else: 
                modseq += pair[0] 
                refseq += pair[1] 


        alignment, score = findalignment(modseq, refseq, filler_chr) 


        modseq = "".ljust(alignment, " ") + modseq 
        refseq = refseq.ljust(len(modseq), " ") 

        max_score = 0 
        seqlen_difference = len(refseq)-len(modseq) 
        for i in multispacestring(modseq,seqlen_difference, filler_chr): 
            score = countmatches(i, refseq) 
            if max_score <= score: 
                max_score = score 
                modseq = i 
    
    alignment_visualisation = "" 

    refseq = refseq.ljust(len(modseq), " ") 

    for modchr, refchr in zip(modseq, refseq): 
        if modchr == refchr: 
            alignment_visualisation += "|" 
        else: 
            alignment_visualisation += "-" 
    
    levenshtein_distance_score = alignment_visualisation.count("-") 

    return refseq, modseq, alignment_visualisation, levenshtein_distance_score 


def images_to_video(folder_path, output_video, fps=30):
    images = [img for img in sorted(os.listdir(folder_path)) if img.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        print("No images found in the specified folder.")
        return
    
    first_image = cv2.imread(os.path.join(folder_path, images[0]))
    height, width, layers = first_image.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    for image in images:
        img_path = os.path.join(folder_path, image)
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Skipping invalid image: {img_path}")
            continue
        frame = cv2.resize(frame, (width, height))  # Ensure consistent size
        video.write(frame)
    
    video.release()
    print(f"Video saved as {output_video}")
