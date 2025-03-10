version 1.0

import "HiFi-human-WGS-WDL/workflows/wdl-common/wdl/workflows/backend_configuration/backend_configuration.wdl" as BackendConfiguration
import "HiFi-human-WGS-WDL/workflows/family.wdl" as FamilyWorkflow

workflow HumanWGS_wrapper {
    input {
        Family family

        File ref_map_file

        String deepvariant_version = "1.6.1"
        File? custom_deepvariant_model_tar

        String pharmcat_version = "2.15.4"
        Int pharmcat_min_coverage = 10

        String phenotypes = "HP:0000001"
        File? tertiary_map_file

        Int? glnexus_mem_gb
        Int? pbsv_call_mem_gb

        Boolean gpu = false

        # Backend configuration
        String backend
        String? zones
        String? gpuType
        String? container_registry
        Boolean preemptible = true

        String? debug_version

        # Wrapper workflow inputs
        String workflow_outputs_bucket
    }

    String workflow_name = "HumanWGS"
    String workflow_version = "v2.1.1"

    call BackendConfiguration.backend_configuration {
        input:
            backend = backend,
            zones = zones,
            gpuType = gpuType,
            container_registry = container_registry
    }

    RuntimeAttributes default_runtime_attributes = if preemptible then backend_configuration.spot_runtime_attributes else backend_configuration.on_demand_runtime_attributes

    String create_timestamp_docker_image = (if (backend == "AWS-HealthOmics") then default_runtime_attributes.container_registry + "/" else "") + "ubuntu:jammy"
    String upload_outputs_docker_image = (if (backend == "AWS-HealthOmics") then default_runtime_attributes.container_registry + "/" else "dnastack/") + "hifi_solves_tools:2.1.0"

    call FamilyWorkflow.humanwgs_family as humanwgs_family {
        input:
            family = family,
            ref_map_file = ref_map_file,
            deepvariant_version = deepvariant_version,
            custom_deepvariant_model_tar = custom_deepvariant_model_tar,
            pharmcat_version = pharmcat_version,
            pharmcat_min_coverage = pharmcat_min_coverage,
            phenotypes = phenotypes,
            tertiary_map_file = tertiary_map_file,
            glnexus_mem_gb = glnexus_mem_gb,
            pbsv_call_mem_gb = pbsv_call_mem_gb,
            gpu = gpu,
            backend = backend,
            zones = zones,
            gpuType = gpuType,
            container_registry = container_registry,
            preemptible = preemptible,
            debug_version = debug_version
    }

    # Create array of workflow output names and their corresponding outputs
    # Each workflow_output_name is at the same index as the corresponding array of workflow_output_files
    Array[String] workflow_output_names = [
      # to maintain order of samples
      "stats_file",

      # bam stats
      "bam_stats",
      "read_length_plot",
      "read_quality_plot",

      # merged, haplotagged alignments
      "merged_haplotagged_bam",
      "merged_haplotagged_bam_index",
      "mapq_distribution_plot",
      "mg_distribution_plot",

      # mosdepth outputs
      "mosdepth_summary",
      "mosdepth_region_bed",
      "mosdepth_region_bed_index",
      "mosdepth_depth_distribution_plot",

      # phasing stats
      "phase_stats",
      "phase_blocks",
      "phase_haplotags",

      # cpg_pileup outputs
      "cpg_combined_bed",
      "cpg_combined_bed_index",
      "cpg_hap1_bed",
      "cpg_hap1_bed_index",
      "cpg_hap2_bed",
      "cpg_hap2_bed_index",
      "cpg_combined_bw",
      "cpg_hap1_bw",
      "cpg_hap2_bw",

      # sv outputs
      "phased_sv_vcf",
      "phased_sv_vcf_index",

      # small variant outputs
      "phased_small_variant_vcf",
      "phased_small_variant_vcf_index",
      "small_variant_gvcf",
      "small_variant_gvcf_index",

      # small variant stats
      "small_variant_stats",
      "bcftools_roh_out",
      "bcftools_roh_bed",
      "snv_distribution_plot",
      "indel_distribution_plot",

      # trgt outputs
      "phased_trgt_vcf",
      "phased_trgt_vcf_index",
      "trgt_spanning_reads",
      "trgt_spanning_reads_index",
      "trgt_coverage_dropouts",

      # paraphase outputs
      "paraphase_output_json",
      "paraphase_realigned_bam",
      "paraphase_realigned_bam_index",
      "paraphase_vcfs",

      # per sample cnv outputs
      "cnv_vcf",
      "cnv_vcf_index",
      "cnv_copynum_bedgraph",
      "cnv_depth_bw",
      "cnv_maf_bw",

      # PGx outputs
      "pbstarphase_json",
      "pharmcat_match_json",
      "pharmcat_phenotype_json",
      "pharmcat_report_html",
      "pharmcat_report_json",

      # joint call outputs
      "joint_small_variants_vcf",
      "joint_small_variants_vcf_index",
      "joint_sv_vcf",
      "joint_sv_vcf_index",
      "joint_trgt_vcf",
      "joint_trgt_vcf_index",

      # tertiary analysis outputs
      "pedigree",
      "tertiary_small_variant_filtered_vcf",
      "tertiary_small_variant_filtered_vcf_index",
      "tertiary_small_variant_filtered_tsv",
      "tertiary_small_variant_compound_het_vcf",
      "tertiary_small_variant_compound_het_vcf_index",
      "tertiary_small_variant_compound_het_tsv",
      "tertiary_sv_filtered_vcf",
      "tertiary_sv_filtered_vcf_index",
      "tertiary_sv_filtered_tsv",
    ]

    Array[Array[File]] workflow_output_files = [
        # to maintain order of samples
        [humanwgs_family.stats_file],

        # bam stats
        humanwgs_family.bam_stats,
        humanwgs_family.read_length_plot,
        select_all(humanwgs_family.read_quality_plot),

        # merged, haplotagged alignments
        humanwgs_family.merged_haplotagged_bam,
        humanwgs_family.merged_haplotagged_bam_index,
        humanwgs_family.mapq_distribution_plot,
        humanwgs_family.mg_distribution_plot,

        # mosdepth outputs
        humanwgs_family.mosdepth_summary,
        humanwgs_family.mosdepth_region_bed,
        humanwgs_family.mosdepth_region_bed_index,
        humanwgs_family.mosdepth_depth_distribution_plot,

        # phasing stats
        humanwgs_family.phase_stats,
        humanwgs_family.phase_blocks,
        humanwgs_family.phase_haplotags,

        # cpg_pileup outputs
        select_all(humanwgs_family.cpg_combined_bed),
        select_all(humanwgs_family.cpg_combined_bed_index),
        select_all(humanwgs_family.cpg_hap1_bed),
        select_all(humanwgs_family.cpg_hap1_bed_index),
        select_all(humanwgs_family.cpg_hap2_bed),
        select_all(humanwgs_family.cpg_hap2_bed_index),
        select_all(humanwgs_family.cpg_combined_bw),
        select_all(humanwgs_family.cpg_hap1_bw),
        select_all(humanwgs_family.cpg_hap2_bw),

        # sv outputs
        humanwgs_family.phased_sv_vcf,
        humanwgs_family.phased_sv_vcf_index,

        # small variant outputs
        humanwgs_family.phased_small_variant_vcf,
        humanwgs_family.phased_small_variant_vcf_index,
        humanwgs_family.small_variant_gvcf,
        humanwgs_family.small_variant_gvcf_index,

        # small variant stats
        humanwgs_family.small_variant_stats,
        humanwgs_family.bcftools_roh_out,
        humanwgs_family.bcftools_roh_bed,
        humanwgs_family.snv_distribution_plot,
        humanwgs_family.indel_distribution_plot,

        # trgt outputs
        humanwgs_family.phased_trgt_vcf,
        humanwgs_family.phased_trgt_vcf_index,
        humanwgs_family.trgt_spanning_reads,
        humanwgs_family.trgt_spanning_reads_index,
        humanwgs_family.trgt_coverage_dropouts,

        # paraphase outputs
        humanwgs_family.paraphase_output_json,
        humanwgs_family.paraphase_realigned_bam,
        humanwgs_family.paraphase_realigned_bam_index,
        select_all(humanwgs_family.paraphase_vcfs),

        # per sample cnv outputs
        humanwgs_family.cnv_vcf,
        humanwgs_family.cnv_vcf_index,
        humanwgs_family.cnv_copynum_bedgraph,
        humanwgs_family.cnv_depth_bw,
        humanwgs_family.cnv_maf_bw,

        # PGx outputs
        humanwgs_family.pbstarphase_json,
        select_all(humanwgs_family.pharmcat_match_json),
        select_all(humanwgs_family.pharmcat_phenotype_json),
        select_all(humanwgs_family.pharmcat_report_html),
        select_all(humanwgs_family.pharmcat_report_json),

        # joint call outputs
        select_all([humanwgs_family.joint_small_variants_vcf]),
        select_all([humanwgs_family.joint_small_variants_vcf_index]),
        select_all([humanwgs_family.joint_sv_vcf]),
        select_all([humanwgs_family.joint_sv_vcf_index]),
        select_all([humanwgs_family.joint_trgt_vcf]),
        select_all([humanwgs_family.joint_trgt_vcf_index]),

        # tertiary analysis outputs
        select_all([humanwgs_family.pedigree]),
        select_all([humanwgs_family.tertiary_small_variant_filtered_vcf]),
        select_all([humanwgs_family.tertiary_small_variant_filtered_vcf_index]),
        select_all([humanwgs_family.tertiary_small_variant_filtered_tsv]),
        select_all([humanwgs_family.tertiary_small_variant_compound_het_vcf]),
        select_all([humanwgs_family.tertiary_small_variant_compound_het_vcf_index]),
        select_all([humanwgs_family.tertiary_small_variant_compound_het_tsv]),
        select_all([humanwgs_family.tertiary_sv_filtered_vcf]),
        select_all([humanwgs_family.tertiary_sv_filtered_vcf_index]),
        select_all([humanwgs_family.tertiary_sv_filtered_tsv]),
    ]

    call create_timestamp {
        input:
            workflow_output_files = workflow_output_files, # !StringCoercion,
            create_timestamp_docker_image = create_timestamp_docker_image,
            runtime_attributes = default_runtime_attributes
    }

    call organize_outputs_and_write_to_bucket as organize_and_write_workflow_outputs {
        input:
            output_names = workflow_output_names,
            output_files = workflow_output_files, # !StringCoercion
            output_type = "workflow",
            backend = backend,
            identifier = family.family_id,
            timestamp = create_timestamp.timestamp,
            workflow_version = workflow_version,
            workflow_name = workflow_name,
            output_bucket = workflow_outputs_bucket,
            upload_outputs_docker_image = upload_outputs_docker_image,
            runtime_attributes = default_runtime_attributes
    }

    Map [String, Array[String]] family_workflow_outputs = read_json(organize_and_write_workflow_outputs.output_manifest_json)

    output {
        # Wrapper workflow outputs
        File workflow_output_json = organize_and_write_workflow_outputs.output_json
        File workflow_output_manifest_tsv = organize_and_write_workflow_outputs.output_manifest_tsv
        File workflow_output_manifest_json = organize_and_write_workflow_outputs.output_manifest_json

        # HumanWGS family workflow outputs
        Array[File] bam_stats = family_workflow_outputs["bam_stats"] # !FileCoercion
        Array[File] read_length_plot = family_workflow_outputs["read_length_plot"] # !FileCoercion
        Array[File] read_quality_plot = family_workflow_outputs["read_quality_plot"] # !FileCoercion
        Array[File] merged_haplotagged_bam = family_workflow_outputs["merged_haplotagged_bam"] # !FileCoercion
        Array[File] merged_haplotagged_bam_index = family_workflow_outputs["merged_haplotagged_bam_index"] # !FileCoercion
        Array[File] mapq_distribution_plot = family_workflow_outputs["mapq_distribution_plot"] # !FileCoercion
        Array[File] mg_distribution_plot = family_workflow_outputs["mg_distribution_plot"] # !FileCoercion
        Array[File] mosdepth_summary = family_workflow_outputs["mosdepth_summary"] # !FileCoercion
        Array[File] mosdepth_region_bed = family_workflow_outputs["mosdepth_region_bed"] # !FileCoercion
        Array[File] mosdepth_region_bed_index = family_workflow_outputs["mosdepth_region_bed_index"] # !FileCoercion
        Array[File] mosdepth_depth_distribution_plot = family_workflow_outputs["mosdepth_depth_distribution_plot"] # !FileCoercion
        Array[File] phase_stats = family_workflow_outputs["phase_stats"] # !FileCoercion
        Array[File] phase_blocks = family_workflow_outputs["phase_blocks"] # !FileCoercion
        Array[File] phase_haplotags = family_workflow_outputs["phase_haplotags"] # !FileCoercion
        Array[File] cpg_combined_bed = family_workflow_outputs["cpg_combined_bed"] # !FileCoercion
        Array[File] cpg_combined_bed_index = family_workflow_outputs["cpg_combined_bed_index"] # !FileCoercion
        Array[File] cpg_hap1_bed = family_workflow_outputs["cpg_hap1_bed"] # !FileCoercion
        Array[File] cpg_hap1_bed_index = family_workflow_outputs["cpg_hap1_bed_index"] # !FileCoercion
        Array[File] cpg_hap2_bed = family_workflow_outputs["cpg_hap2_bed"] # !FileCoercion
        Array[File] cpg_hap2_bed_index = family_workflow_outputs["cpg_hap2_bed_index"] # !FileCoercion
        Array[File] cpg_combined_bw = family_workflow_outputs["cpg_combined_bw"] # !FileCoercion
        Array[File] cpg_hap1_bw = family_workflow_outputs["cpg_hap1_bw"] # !FileCoercion
        Array[File] cpg_hap2_bw = family_workflow_outputs["cpg_hap2_bw"] # !FileCoercion
        Array[File] phased_sv_vcf = family_workflow_outputs["phased_sv_vcf"] # !FileCoercion
        Array[File] phased_sv_vcf_index = family_workflow_outputs["phased_sv_vcf_index"] # !FileCoercion
        Array[File] phased_small_variant_vcf = family_workflow_outputs["phased_small_variant_vcf"] # !FileCoercion
        Array[File] phased_small_variant_vcf_index = family_workflow_outputs["phased_small_variant_vcf_index"] # !FileCoercion
        Array[File] small_variant_gvcf = family_workflow_outputs["small_variant_gvcf"] # !FileCoercion
        Array[File] small_variant_gvcf_index = family_workflow_outputs["small_variant_gvcf_index"] # !FileCoercion
        Array[File] small_variant_stats = family_workflow_outputs["small_variant_stats"] # !FileCoercion
        Array[File] bcftools_roh_out = family_workflow_outputs["bcftools_roh_out"] # !FileCoercion
        Array[File] bcftools_roh_bed = family_workflow_outputs["bcftools_roh_bed"] # !FileCoercion
        Array[File] snv_distribution_plot = family_workflow_outputs["snv_distribution_plot"] # !FileCoercion
        Array[File] indel_distribution_plot = family_workflow_outputs["indel_distribution_plot"] # !FileCoercion
        Array[File] phased_trgt_vcf = family_workflow_outputs["phased_trgt_vcf"] # !FileCoercion
        Array[File] phased_trgt_vcf_index = family_workflow_outputs["phased_trgt_vcf_index"] # !FileCoercion
        Array[File] trgt_spanning_reads = family_workflow_outputs["trgt_spanning_reads"] # !FileCoercion
        Array[File] trgt_spanning_reads_index = family_workflow_outputs["trgt_spanning_reads_index"] # !FileCoercion
        Array[File] trgt_coverage_dropouts = family_workflow_outputs["trgt_coverage_dropouts"] # !FileCoercion
        Array[File] paraphase_output_json = family_workflow_outputs["paraphase_output_json"] # !FileCoercion
        Array[File] paraphase_realigned_bam = family_workflow_outputs["paraphase_realigned_bam"] # !FileCoercion
        Array[File] paraphase_realigned_bam_index = family_workflow_outputs["paraphase_realigned_bam_index"] # !FileCoercion
        Array[File] paraphase_vcfs = family_workflow_outputs["paraphase_vcfs"] # !FileCoercion
        Array[File] cnv_vcf = family_workflow_outputs["cnv_vcf"] # !FileCoercion
        Array[File] cnv_vcf_index = family_workflow_outputs["cnv_vcf_index"] # !FileCoercion
        Array[File] cnv_copynum_bedgraph = family_workflow_outputs["cnv_copynum_bedgraph"] # !FileCoercion
        Array[File] cnv_depth_bw = family_workflow_outputs["cnv_depth_bw"] # !FileCoercion
        Array[File] cnv_maf_bw = family_workflow_outputs["cnv_maf_bw"] # !FileCoercion
        Array[File] pbstarphase_json = family_workflow_outputs["pbstarphase_json"] # !FileCoercion
        Array[File] pharmcat_match_json = family_workflow_outputs["pharmcat_match_json"] # !FileCoercion
        Array[File] pharmcat_phenotype_json = family_workflow_outputs["pharmcat_phenotype_json"] # !FileCoercion
        Array[File] pharmcat_report_html = family_workflow_outputs["pharmcat_report_html"] # !FileCoercion
        Array[File] pharmcat_report_json = family_workflow_outputs["pharmcat_report_json"] # !FileCoercion
        Array[File] joint_small_variants_vcf = family_workflow_outputs["joint_small_variants_vcf"] # !FileCoercion
        Array[File] joint_small_variants_vcf_index = family_workflow_outputs["joint_small_variants_vcf_index"] # !FileCoercion
        Array[File] joint_sv_vcf = family_workflow_outputs["joint_sv_vcf"] # !FileCoercion
        Array[File] joint_sv_vcf_index = family_workflow_outputs["joint_sv_vcf_index"] # !FileCoercion
        Array[File] joint_trgt_vcf = family_workflow_outputs["joint_trgt_vcf"] # !FileCoercion
        Array[File] joint_trgt_vcf_index = family_workflow_outputs["joint_trgt_vcf_index"] # !FileCoercion
        Array[File] pedigree = family_workflow_outputs["pedigree"] # !FileCoercion
        Array[File] tertiary_small_variant_filtered_vcf = family_workflow_outputs["tertiary_small_variant_filtered_vcf"] # !FileCoercion
        Array[File] tertiary_small_variant_filtered_vcf_index = family_workflow_outputs["tertiary_small_variant_filtered_vcf_index"] # !FileCoercion
        Array[File] tertiary_small_variant_filtered_tsv = family_workflow_outputs["tertiary_small_variant_filtered_tsv"] # !FileCoercion
        Array[File] tertiary_small_variant_compound_het_vcf = family_workflow_outputs["tertiary_small_variant_compound_het_vcf"] # !FileCoercion
        Array[File] tertiary_small_variant_compound_het_vcf_index = family_workflow_outputs["tertiary_small_variant_compound_het_vcf_index"] # !FileCoercion
        Array[File] tertiary_small_variant_compound_het_tsv = family_workflow_outputs["tertiary_small_variant_compound_het_tsv"] # !FileCoercion
        Array[File] family_tertiary_sv_filtered_vcf = family_workflow_outputs["tertiary_sv_filtered_vcf"] # !FileCoercion
        Array[File] family_tertiary_sv_filtered_vcf_index = family_workflow_outputs["tertiary_sv_filtered_vcf_index"] # !FileCoercion
        Array[File] family_tertiary_sv_filtered_tsv = family_workflow_outputs["tertiary_sv_filtered_tsv"] # !FileCoercion
    }

    parameter_meta {
        workflow_outputs_bucket: {help: "Path to the bucket where the workflow outputs will be stored"}
    }
}

task create_timestamp {
    input {
        Array[Array[String]] workflow_output_files
        String create_timestamp_docker_image

        RuntimeAttributes runtime_attributes
    }

    command <<<
        set -euo pipefail

        date +%s > timestamp.txt

        echo -e "Created timestamp for outputs\n~{sep='\n' flatten(workflow_output_files)}"
    >>>

    output {
        String timestamp = read_string("timestamp.txt")
    }

    runtime {
        docker: create_timestamp_docker_image
        cpu: 2
        memory: "4 GB"
        disk: "15 GB"
        disks: "local-disk 15 HDD"
        preemptible: runtime_attributes.preemptible_tries
        zones: runtime_attributes.zones
    }
}

task organize_outputs_and_write_to_bucket {
    input {
        Array[String] output_names
        Array[Array[String]] output_files
        String output_type
        String backend
        String identifier
        String timestamp
        String workflow_version
        String workflow_name
        String output_bucket
        String upload_outputs_docker_image

        RuntimeAttributes runtime_attributes
    }

    command <<<
        set -euo pipefail

        cp ~{write_lines(output_names)} output_names.txt
        cp ~{write_tsv(output_files)} output_files.tsv

        files_to_json.py \
            -n output_names.txt \
            -f output_files.tsv \
            -j ~{identifier}.~{output_type}_outputs.json

        upload_outputs.sh \
            -b ~{backend} \
            -i ~{identifier} \
            -t ~{timestamp} \
            -w ~{workflow_name} \
            -v ~{workflow_version} \
            -o ~{output_bucket} \
            -j ~{identifier}.~{output_type}_outputs.json \
            -p ~{identifier}.~{output_type}_outputs
    >>>

    output {
        File output_json = "~{identifier}.~{output_type}_outputs.json"
        File output_manifest_tsv = "~{identifier}.~{output_type}_outputs.manifest.tsv"
        File output_manifest_json = "~{identifier}.~{output_type}_outputs.manifest.json"
    }

    runtime {
        docker: upload_outputs_docker_image
        cpu: 2
        memory: "4 GB"
        disk: "50 GB"
        disks: "local-disk 50 HDD"
        bootDiskSizeGb: 20
        preemptible: runtime_attributes.preemptible_tries
        zones: runtime_attributes.zones
    }
}
