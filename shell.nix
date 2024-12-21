{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {

  buildInputs = with pkgs; [
    python311
  ] ++ (with python311Packages;
    [
      numpy
    ]);


  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH
  '';
}
