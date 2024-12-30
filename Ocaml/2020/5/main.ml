let rec compute (i0: int) (i1: int) (j0: int) (j1: int) : char list -> (int*int) = function
  |[] -> (i0, j0)
  |c::q -> 
    match c with
      |'F' -> compute i0 ((i0 + i1) / 2) j0 j1 q
      |'B' -> compute ((i0 + i1) / 2 + 1) i1 j0 j1 q
      |'L' -> compute i0 i1 j0 ((j0 + j1) / 2) q
      |'R' -> compute i0 i1 ((j0 + j1) / 2 + 1) j1 q
      |s -> failwith (Printf.sprintf "Unknown character: %c" s)
  
let rec find_max (acc: int) : int list -> int = function
  |[] -> acc
  |t::q ->
    if t > acc
    then find_max t q
    else find_max acc q

let rec is_in (x: 'a) : 'a list -> bool = function
  |[] -> false
  |t::q ->
    if t = x
    then true
    else is_in x q

let rec draw : int list -> unit = function
  |[] -> ()
  |t::q ->
    Printf.printf "%d; " t;
    draw q

let rec main1 (l: string list list) : int =
  let passes = List.map (fun l -> List.of_seq (String.to_seq (List.hd l))) l in
  let seats = List.map (fun p -> compute 0 127 0 7 p) passes in
  let ids = List.map (fun (i, j) -> 8 * i + j) seats in
  find_max 0 ids

let rec main2 (l: string list list) : int =
  let passes = List.map (fun l -> List.of_seq (String.to_seq (List.hd l))) l in
  let seats = List.map (fun p -> compute 0 127 0 7 p) passes in
  let ids = List.map (fun (i, j) -> 8 * i + j) seats in
  let valid_seats = ref [] in
  for i = 1 to 1022 do
    if is_in i ids
    then ()
    else valid_seats := i::(!valid_seats);
  done;
  draw (List.rev !valid_seats);
  List.hd (List.rev !valid_seats)

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_string_list (Parse.parse "2020/5/test.txt" false)
    else
      Parse.convert_to_string_list (Parse.parse "2020/5/data.txt" false)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x