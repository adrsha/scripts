{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.dbus-python 
    python3Packages.pygobject3
  ];
}
