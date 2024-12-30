let rec parcours (i: int) : string list list -> int = function
  |[] -> 0
  |[]::q -> parcours i q
  |[s]::q -> (
    let l = Array.of_seq (String.to_seq s) in
    let size = Array.length l in
    let j = (i+3) mod size in
    if l.(j) = '#'
    then 1 + (parcours (j) q)
    else parcours (j) q
  )
  |_ -> failwith "Parsing error"

let rec param_parcours (di: int) (dj: int) (i_acc: int) (j_acc: int) : string list list -> int = function
    |[] -> 0
    |[]::q -> param_parcours di dj i_acc j_acc q
    |[s]::q when j_acc = 0 -> (
      let l = Array.of_seq (String.to_seq s) in
      let size = Array.length l in
      let i_incr = (i_acc + di) mod size in
      let increment =
        if l.(i_incr) = '#'
        then 1
        else 0
      in
      (param_parcours di dj i_incr (dj-1) q) + increment
    )
    |_::q ->
      param_parcours di dj i_acc (j_acc - 1) q

let rec main1 (l: string list list) : int =
  parcours (-3) l

let rec main2 (l: string list list) : int =
  let rec aux (acc: int) (l: string list list): (int*int) list -> int = function
    |[] -> acc
    |(di, dj)::q ->
      aux (acc*(param_parcours di dj 0 dj l)) l q
  in
  aux 1 l [
    (1, 1);
    (3, 1);
    (5, 1);
    (7, 1);
    (1, 2);
  ]

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_string_list (Parse.parse "2020/3/test.txt" false)
    else
      Parse.convert_to_string_list (Parse.parse "2020/3/data.txt" false)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x