{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312      # Tambahkan Python 3.12
    pkgs.docker
  ];
}

# file ini untuk development di google idx