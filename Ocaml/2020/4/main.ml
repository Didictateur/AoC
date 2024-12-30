let attribute = [
  "byr";
  "iyr";
  "eyr";
  "hgt";
  "hcl";
  "ecl";
  "pid";
  (* "cid"; *)
]

let rec group_by (acc: 'a list) (l: 'a list list) : 'a list list -> 'a list list = function
  |[] -> acc::l
  |[]::q -> (
      (* Printf.printf "grouping\n"; *)
      group_by [] (acc::l) q
    )
  |t::q -> (
      (* Printf.printf "l: %s\n" (List.hd t); *)
      group_by (acc@t) l q
    )

let rec purify : string list list -> string list list = function
  |[] -> []
  |t::q ->
    let purified_t = List.map (fun s -> List.hd (String.split_on_char ':' s)) t in
    purified_t :: (purify q)
  
let rec purify_c : string list list -> (string*string) list list = function
  |[] -> []
  |t::q ->
    let pair = List.map (fun s ->
      match String.split_on_char ':' s with
        |[k; v] -> (k, v)
        |_ -> failwith (Printf.sprintf "Invalid format with %s" s)
    ) t in
    pair::(purify_c q)

let rec is_in (x: 'a) : 'a list -> bool = function
  |[] -> false
  |t::q when t = x -> true
  |_::q -> is_in x q

let rec has_all (l: 'a list) : 'a list -> bool = function
  |[] -> true
  |t::q ->
    if is_in t l
    then has_all l q
    else (
      (* Printf.printf "Has not %s\n" t; *)
      false
    )
  
let parse_height (height: string) : int*string*bool =
  let re = Str.regexp "\\([0-9]+\\)\\(in\\|cm\\)" in
  if Str.string_match re height 0 then
    let value = int_of_string (Str.matched_group 1 height) in
    let unit = Str.matched_group 2 height in
    (value, unit, true)
  else
    (0, "", false)

let rec is_hexa : char list -> bool = function
  |[] -> true
  |t::q ->
    if is_in t ['0';'1';'2';'3';'4';'5';'6';'7';'8';'9';'a';'b';'c';'d';'e';'f']
    then is_hexa q
    else false

let rec is_valide : (string*string) list -> bool = function
  |[] -> true
  |(key, value)::q -> (
    match (key, value) with
      |("byr", v) ->
        let bth = int_of_string v in
        if 1920 <= bth && bth <= 2002
        then is_valide q
        else (
          (* Printf.printf "Invalid birthday: %d\n" bth; *)
          false
        )
      |("iyr", v) ->
        let year = int_of_string v in
        if 2010 <= year && year <= 2020
        then is_valide q
        else (
          (* Printf.printf "Invalid issue year: %d\n" year; *)
          false
        )
      |("eyr", v) ->
        let year = int_of_string v in
        if 2020 <= year && year <= 2030
        then is_valide q
        else (
          (* Printf.printf "Invalid expiration year: %d\n" year; *)
          false
        )
      |("hgt", v) ->
        let (h, u, b) = parse_height v in
        if b
        then
          if u = "cm"
          then (
            if 150 <= h && h <= 193
            then is_valide q
            else (
              (* Printf.printf "Invalid heigth :%s\n" v; *)
              false
            )
          )
          else (
            if 59 <= h && h <= 76
            then is_valide q
            else (
              (* Printf.printf "Invalid heigth :%s\n" v; *)
              false
            )
          )
        else (
          (* Printf.printf "Invalid heigth :%s\n" v; *)
          false
        )
      |("hcl", v) ->
        if String.length v <> 7
        then (
          (* Printf.printf "Invalid hair color: %s\n" v; *)
          false
        )
        else (
          let t::hex = List.of_seq (String.to_seq v) in
          if t <> '#'
          then (
            (* Printf.printf "Invalid hair color: %s\n" v; *)
            false
          )
          else (
            if is_hexa hex
            then is_valide q
            else (
              (* Printf.printf "Invalid hair color: %s\n" v; *)
              false
            )
          )
        )
      |("ecl", v) ->
        if is_in v ["amb"; "blu"; "brn"; "gry"; "grn"; "hzl"; "oth"]
        then is_valide q
        else (
          (* Printf.printf "Invalid eye color: %s\n" v; *)
          false
        )
      |("pid", v) ->
        if String.length v = 9
        then is_valide q
        else (
          (* Printf.printf "Invalid ID password: %s\n" v; *)
          false
        )
      |_ -> (
        
        is_valide q
      )
  )

let rec count1 : 'a list list -> int = function
  |[] -> 0
  |t::q ->
    if has_all t attribute
    then 1 + (count1 q)
    else (
      (* Printf.printf "failed\n"; *)
      count1 q
    )
  
let rec count2 : (string*string) list list -> int = function
  |[] -> 0
  |t::q ->
    if has_all (List.map (fun (k, v) -> k) t) attribute && is_valide t
    then 1 + (count2 q)
    else (
      (* Printf.printf "failed\n"; *)
      count2 q
    )

let rec main1 (l: string list list) : int =
  let group = group_by [] [] l in
  (* Printf.printf "length: %d\n" (List.length group); *)
  count1 (purify group)

let rec main2 (l: string list list) : int =
  let group = group_by [] [] l in
  (* Printf.printf "length: %d\n" (List.length group); *)
  count2 (purify_c group)

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_string_list (Parse.parse "2020/4/test.txt" false)
    else
      Parse.convert_to_string_list (Parse.parse "2020/4/data.txt" false)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x