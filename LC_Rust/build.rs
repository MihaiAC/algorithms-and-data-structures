use std::collections::HashSet;
use std::fs;
use std::path::Path;

fn main() {
    fs::create_dir_all("src/bin").unwrap();

    let mut generated: HashSet<String> = HashSet::new();

    for difficulty in ["easy", "medium", "hard"] {
        println!("cargo:rerun-if-changed={difficulty}");

        let dir = Path::new(difficulty);
        if !dir.exists() {
            continue;
        }

        for entry in fs::read_dir(dir).unwrap().flatten() {
            let path = entry.path();
            if path.extension().is_some_and(|ext| ext == "rs") {
                let stem = path.file_stem().unwrap().to_str().unwrap().to_owned();
                let stub_path = format!("src/bin/{stem}.rs");
                let content = format!("include!(\"../../{difficulty}/{stem}.rs\");\n");
                if fs::read_to_string(&stub_path).ok().as_deref() != Some(&content) {
                    fs::write(&stub_path, &content).unwrap();
                }
                generated.insert(stem);
            }
        }
    }

    // Remove stubs for deleted solution files
    for entry in fs::read_dir("src/bin").unwrap().flatten() {
        let path = entry.path();
        if path.extension().is_some_and(|ext| ext == "rs") {
            let stem = path.file_stem().unwrap().to_str().unwrap().to_owned();
            if !generated.contains(&stem) {
                fs::remove_file(&path).unwrap();
            }
        }
    }
}
