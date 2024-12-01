
let
  pkgs = import <nixpkgs> { };
in
  pkgs.mkShell {
    packages = [
      pkgs.htmlq
      pkgs.python3Packages.parse
      pkgs.python3Packages.networkx
      pkgs.python3Packages.numpy
      pkgs.python3Packages.sympy
    ];
  }
