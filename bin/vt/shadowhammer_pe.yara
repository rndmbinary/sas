import "pe"
import "hash"

rule shadowhammer_pe_section
{
	meta:
		description = "Rule for sofacy discovery based on .data section"
		author = "Scott Gordon"
		date = "27 MAR 2019"
    		ref = "aa15eb28292321b586c27d8401703494"
  	condition:
    		for any i in (0..pe.number_of_sections - 1): (
    		hash.md5(pe.sections[i].raw_data_offset, 
        	pe.sections[i].raw_data_size) == 
        	"7d3fc4823b27cc8e308ae19677167351" and 
        	pe.sections[i].name ==".data")
}
