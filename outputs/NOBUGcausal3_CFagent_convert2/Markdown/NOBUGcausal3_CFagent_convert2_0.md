
# Parameters

    Name :                      NOBUGcausal3_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      33965949603 function calls (33743317160 primitive calls) in 57316.77 seconds

##    Ordered by: cumulative time
   List reduced from 489 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57316.773 57316.773 {built-in method builtins.exec}
                      1    4.558    4.558 57316.773 57316.773 <string>:1(<module>)
                      1  158.118  158.118 57312.215 57312.215 main.py:96(CFagent)
                7104783   27.090    0.000 22139.711    0.003 agent.py:28(learn)
                7104776  542.233    0.000 18573.735    0.003 learner.py:42(Qlearn)
                2368261   11.943    0.000 9452.038    0.004 game.py:36(step)
        249077511/26446759 1063.049    0.000 9432.616    0.000 module.py:866(_call_impl)
                2368261   14.358    0.000 8910.519    0.004 layers.py:594(step)
               19341983   54.599    0.000 8843.195    0.000 network.py:24(forward)
               19341983  279.070    0.000 8662.682    0.000 container.py:117(forward)
                2368261  227.472    0.000 8512.613    0.004 agent.py:53(_learn)
                2368261  224.962    0.000 7904.273    0.003 agent.py:191(_learn)
                7104776   63.632    0.000 7875.441    0.001 optimizer.py:84(wrapper)
                7104776   33.487    0.000 7570.573    0.001 grad_mode.py:24(decorate_context)
                7104776  218.118    0.000 7468.548    0.001 adam.py:55(step)
                7104776 1538.422    0.000 7007.956    0.001 _functional.py:53(adam)
                2368261  747.419    0.000 6263.142    0.003 agent.py:199(counterfact)
                2368261  205.136    0.000 5795.963    0.002 layers.py:18(step)
                2368261   68.565    0.000 5679.419    0.002 agent.py:114(_learn)
              232867357  305.409    0.000 5568.566    0.000 layer.py:82(move)
                2368261 2592.644    0.001 4927.561    0.002 replaybuffer.py:28(teleporter_save_data)
                7104776   37.776    0.000 4730.981    0.001 tensor.py:195(backward)
                7104776   30.962    0.000 4692.015    0.001 __init__.py:68(backward)
                6117467  148.204    0.000 4509.206    0.001 agent.py:48(__call__)
                7104776 4497.091    0.001 4497.091    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2368261 2087.333    0.001 3824.715    0.002 agent.py:85(interveen)
              232867357  542.288    0.000 3250.458    0.000 layers.py:611(check)
                2368261 2387.597    0.001 3220.221    0.001 replaybuffer.py:22(sample_data)
               38683966   90.568    0.000 3114.661    0.000 conv.py:398(forward)
                2368262  259.755    0.000 3081.156    0.001 layers.py:565(update)
               33771440 3013.714    0.000 3013.714    0.000 {built-in method tensor}
               38683966   53.652    0.000 2983.475    0.000 conv.py:390(_conv_forward)
               38683966 2929.823    0.000 2929.823    0.000 {built-in method conv2d}
               28228755   21.821    0.000 2853.078    0.000 game.py:32(board)
                2368261 2063.536    0.001 2810.819    0.001 replaybuffer.py:49(sample_data)
               53289427  122.333    0.000 2500.770    0.000 linear.py:93(forward)
               53289427   46.429    0.000 2323.134    0.000 functional.py:1737(linear)
               53289427 2265.328    0.000 2265.328    0.000 {built-in method torch._C._nn.linear}
               37892184 1248.337    0.000 2252.326    0.000 layer.py:143(NoRock_update)
              162663604 2170.356    0.000 2170.356    0.000 {built-in method clone}
                2368261 1126.369    0.000 1875.323    0.001 agent.py:66(modify)
              232782681  326.899    0.000 1760.264    0.000 layers.py:605(isFree)
                1383225   13.843    0.000 1705.595    0.001 agent.py:167(choose_action)
             1556641493 1190.441    0.000 1433.365    0.000 layer.py:79(isFree)
              132622476 1410.632    0.000 1410.632    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               72631410   59.390    0.000 1391.341    0.000 activation.py:713(forward)
               34536564 1378.671    0.000 1378.671    0.000 {built-in method cat}
               72631410   65.451    0.000 1331.951    0.000 functional.py:1364(leaky_relu)
              132622476 1255.177    0.000 1255.177    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               72631410 1253.985    0.000 1253.985    0.000 {built-in method torch._C._nn.leaky_relu}
                8485728   62.196    0.000 1246.172    0.000 agent.py:58(modify_board)
                2368254   37.598    0.000 1221.413    0.001 agent.py:163(__call__)
                2368261   36.442    0.000 1149.753    0.000 agent.py:109(__call__)
                7104776  178.188    0.000 1100.504    0.000 optimizer.py:189(zero_grad)
                3162920   30.304    0.000  915.525    0.000 layers.py:615(restart)
             3191044226  561.136    0.000  821.557    0.000 enum.py:646(__hash__)
               66311238  813.894    0.000  813.894    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8485728  784.016    0.000  784.016    0.000 {built-in method torch._C._nn.one_hot}
              232867357  485.295    0.000  782.113    0.000 layers.py:303(check)
                2368261  313.567    0.000  745.410    0.000 replaybuffer.py:55(CF_save_data)
              232867357  438.008    0.000  731.618    0.000 layers.py:262(check)
               66311238  680.665    0.000  680.665    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2368261   50.365    0.000  662.957    0.000 replaybuffer.py:18(stacker)
              236826200   80.224    0.000  654.796    0.000 {built-in method builtins.all}
               66311238  647.965    0.000  647.965    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               66311238  640.840    0.000  640.840    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3162920   16.514    0.000  624.408    0.000 level.py:8(__init__)
              735302046  181.618    0.000  603.015    0.000 layers.py:571(<genexpr>)
                2368254   49.170    0.000  580.655    0.000 replaybuffer.py:45(stacker)
              803593910  565.972    0.000  565.972    0.000 layer.py:122(elements)
              173517586  540.493    0.000  540.493    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2368261  305.487    0.000  504.588    0.000 collector.py:54(collect)
               66311238  499.780    0.000  499.780    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3162920   65.746    0.000  497.727    0.000 levels.py:164(generate)
                6117467  172.836    0.000  470.781    0.000 exploration.py:53(softmaxer)
              232867357  270.649    0.000  419.548    0.000 layers.py:329(check)
              464178750  332.664    0.000  410.162    0.000 tensor.py:906(grad)
              236826200  264.384    0.000  395.164    0.000 layers.py:111(isDone)
               11062362  146.516    0.000  388.786    0.000 random.py:315(sample)
             4042847371  387.544    0.000  387.544    0.000 layer.py:75(positions)
              232867357  241.077    0.000  379.774    0.000 layers.py:288(check)
        4592636890/4592636887  323.911    0.000  372.580    0.000 {built-in method builtins.len}
                7104776   10.705    0.000  356.860    0.000 loss.py:527(forward)
                7104776   26.970    0.000  346.155    0.000 functional.py:2898(mse_loss)
                6325840   52.360    0.000  345.040    0.000 level.py:41(notUsed)
              232867357  218.981    0.000  331.884    0.000 layers.py:47(check)
                7104784  315.978    0.000  315.978    0.000 {built-in method nonzero}
             3191071361  260.426    0.000  260.426    0.000 {built-in method builtins.hash}
               25303360   31.521    0.000  252.030    0.000 layer.py:56(restart)
               38683966   28.211    0.000  231.119    0.000 flatten.py:39(forward)
                7104776  229.651    0.000  229.651    0.000 {built-in method torch._C._nn.mse_loss}
               14209566  210.575    0.000  210.575    0.000 {built-in method sum}
              204659207  151.983    0.000  205.766    0.000 layer.py:102(remove)
              364857684  151.171    0.000  204.504    0.000 layer.py:106(add)
               38683966  202.909    0.000  202.909    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7105623  200.439    0.000  200.439    0.000 {built-in method max}
              303687206  134.398    0.000  197.317    0.000 random.py:250(_randbelow_with_getrandbits)
              255198480  181.167    0.000  181.167    0.000 {built-in method torch._C._get_tracing_state}
                9473037   15.037    0.000  177.599    0.000 tensor.py:525(__rsub__)
                3163020   80.532    0.000  161.237    0.000 layers.py:33(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9494239: <NOBUGcausal3_CFagent_convert2_0> in cluster <dcc> Done

Job <NOBUGcausal3_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:52 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:24 2021
Results reported at Sun Apr  4 18:55:24 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   57278.64 sec.
    Max Memory :                                 3579 MB
    Average Memory :                             3536.81 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12805.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57363 sec.
    Turnaround time :                            57332 sec.

The output (if any) is above this job summary.

