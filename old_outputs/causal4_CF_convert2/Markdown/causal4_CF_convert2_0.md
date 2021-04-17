
# Parameters

    Name :                      causal4_CF_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
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


      45617677119 function calls (45370291724 primitive calls) in 57313.67 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57313.672 57313.672 {built-in method builtins.exec}
                      1    4.756    4.756 57313.671 57313.671 <string>:1(<module>)
                      1  174.852  174.852 57308.916 57308.916 main.py:96(CFagent)
                8272146   28.977    0.000 19866.660    0.002 agent.py:29(learn)
                8272128  505.864    0.000 16188.642    0.002 learner.py:42(Qlearn)
                2757382   12.026    0.000 13176.516    0.005 game.py:35(step)
                2757382   15.640    0.000 12556.558    0.005 layers.py:448(step)
                2757382  243.707    0.000 9019.173    0.003 layers.py:17(step)
        277190268/29806564 1076.767    0.000 8909.661    0.000 module.py:866(_call_impl)
              275395868  674.490    0.000 8749.243    0.000 layer.py:84(move)
               21534436   59.989    0.000 8322.226    0.000 network.py:24(forward)
               21534436  275.024    0.000 8127.404    0.000 container.py:117(forward)
                2757382  280.024    0.000 7719.412    0.003 agent.py:54(_learn)
                2757382  278.007    0.000 7091.292    0.003 agent.py:193(_learn)
                2757382  508.864    0.000 7032.682    0.003 agent.py:201(counterfact)
                8272128   71.373    0.000 6423.367    0.001 optimizer.py:84(wrapper)
                8272128   36.310    0.000 6113.114    0.001 grad_mode.py:24(decorate_context)
                8272128  240.072    0.000 6000.652    0.001 adam.py:55(step)
                8272128 1284.045    0.000 5484.552    0.001 _functional.py:53(adam)
              275395868  864.387    0.000 5209.763    0.000 layers.py:465(check)
                2757382   84.485    0.000 5009.089    0.002 agent.py:115(_learn)
               42539954 4227.321    0.000 4227.321    0.000 {built-in method tensor}
                6627776  167.913    0.000 4182.356    0.001 agent.py:49(__call__)
                8272128   32.620    0.000 4110.182    0.000 tensor.py:195(backward)
                8272128   32.208    0.000 4076.300    0.000 __init__.py:68(backward)
               36139227   23.013    0.000 4075.576    0.000 game.py:31(board)
                8272128 3882.897    0.000 3882.897    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2757382 2846.757    0.001 3758.154    0.001 replaybuffer.py:22(sample_data)
                2757383  288.074    0.000 3500.064    0.001 layers.py:419(update)
               55147650 1911.622    0.000 3338.816    0.000 layer.py:129(update)
                2757382 2400.923    0.001 3204.662    0.001 replaybuffer.py:49(sample_data)
                2757382 1689.223    0.001 3028.732    0.001 replaybuffer.py:28(teleporter_save_data)
                2757382 1291.024    0.000 3016.863    0.001 agent.py:86(interveen)
               43068872   97.579    0.000 3007.869    0.000 conv.py:398(forward)
               43068872   61.384    0.000 2866.587    0.000 conv.py:390(_conv_forward)
               43068872 2805.203    0.000 2805.203    0.000 {built-in method conv2d}
              275237853  485.408    0.000 2407.056    0.000 layers.py:459(isFree)
               59088544  119.221    0.000 2287.591    0.000 linear.py:93(forward)
               59088544   49.826    0.000 2109.234    0.000 functional.py:1737(linear)
               59088544 2046.935    0.000 2046.935    0.000 {built-in method torch._C._nn.linear}
             2343875834 1547.470    0.000 1921.647    0.000 layer.py:81(isFree)
                2757382 1019.060    0.000 1726.196    0.001 agent.py:67(modify)
               39716270 1419.531    0.000 1419.531    0.000 {built-in method cat}
              128194376 1266.683    0.000 1266.683    0.000 {built-in method clone}
               80622980   65.696    0.000 1229.737    0.000 activation.py:713(forward)
                1119786   20.813    0.000 1212.445    0.001 agent.py:168(choose_action)
                2757364   44.275    0.000 1210.457    0.000 agent.py:164(__call__)
                9385158   60.392    0.000 1176.099    0.000 agent.py:59(modify_board)
               80622980   68.330    0.000 1164.040    0.000 functional.py:1364(leaky_relu)
                2757382   42.102    0.000 1149.974    0.000 agent.py:110(__call__)
             4410937836  764.599    0.000 1104.315    0.000 enum.py:646(__hash__)
               80622980 1082.411    0.000 1082.411    0.000 {built-in method torch._C._nn.leaky_relu}
              154413032 1072.488    0.000 1072.488    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              154413032  952.190    0.000  952.190    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8272128  166.707    0.000  937.998    0.000 optimizer.py:189(zero_grad)
              275395868  552.843    0.000  879.228    0.000 layers.py:270(check)
              275395868  488.415    0.000  806.178    0.000 layers.py:233(check)
              275395868  616.963    0.000  801.147    0.000 layers.py:67(check)
              817259660  779.346    0.000  779.346    0.000 layer.py:124(elements)
                9385158  765.237    0.000  765.237    0.000 {built-in method torch._C._nn.one_hot}
                2757382   58.923    0.000  716.467    0.000 replaybuffer.py:18(stacker)
              275738300  139.329    0.000  680.488    0.000 {built-in method builtins.all}
                1930858   23.970    0.000  645.579    0.000 layers.py:469(restart)
               77206516  627.150    0.000  627.150    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2757364   55.814    0.000  614.345    0.000 replaybuffer.py:45(stacker)
             6111477933  574.984    0.000  574.984    0.000 layer.py:77(positions)
             1460829631  356.100    0.000  573.723    0.000 layers.py:425(<genexpr>)
               77206516  543.802    0.000  543.802    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              275395868  393.634    0.000  519.637    0.000 layers.py:56(check)
               77206516  494.910    0.000  494.910    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               77206516  489.213    0.000  489.213    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        6755150732/6755150729  420.992    0.000  472.914    0.000 {built-in method builtins.len}
              275395868  303.269    0.000  472.864    0.000 layers.py:257(check)
                2757382  163.949    0.000  442.661    0.000 replaybuffer.py:55(CF_save_data)
                1930858   10.636    0.000  437.598    0.000 level.py:8(__init__)
              540445696  351.159    0.000  434.644    0.000 tensor.py:906(grad)
                2757382  249.847    0.000  420.809    0.000 collector.py:54(collect)
              275395868  269.411    0.000  420.581    0.000 layers.py:294(check)
                6627776  157.119    0.000  414.687    0.000 exploration.py:53(softmaxer)
                9376480  153.011    0.000  405.133    0.000 random.py:315(sample)
              275395868  245.895    0.000  375.256    0.000 layers.py:42(check)
               77206516  373.468    0.000  373.468    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1930858   64.323    0.000  358.381    0.000 levels.py:199(generate)
                8272128   11.185    0.000  351.274    0.000 loss.py:527(forward)
                8272128   35.196    0.000  340.089    0.000 functional.py:2898(mse_loss)
             4410969339  339.722    0.000  339.722    0.000 {built-in method builtins.hash}
                8272147  315.752    0.000  315.752    0.000 {built-in method nonzero}
              140336898  281.952    0.000  281.952    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3861716   28.443    0.000  231.668    0.000 level.py:41(notUsed)
              238135965  150.325    0.000  212.678    0.000 layer.py:104(remove)
              329104264  141.871    0.000  209.371    0.000 random.py:250(_randbelow_with_getrandbits)
                8272128  207.470    0.000  207.470    0.000 {built-in method torch._C._nn.mse_loss}
               55147650  207.311    0.000  207.311    0.000 layer.py:141(<listcomp>)
               43068872   30.151    0.000  202.236    0.000 flatten.py:39(forward)
              353792564  149.100    0.000  201.981    0.000 layer.py:108(add)
             1852167796  194.375    0.000  194.375    0.000 layer.py:181(isBlocking)
                8273065  190.529    0.000  190.529    0.000 {built-in method max}
               16544292  177.697    0.000  177.697    0.000 {built-in method sum}
               19308580   27.200    0.000  177.380    0.000 layer.py:58(restart)
               43068872  172.085    0.000  172.085    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 9495292: <causal4_CF_convert2_0> in cluster <dcc> Done

Job <causal4_CF_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:26 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 02:37:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 02:37:27 2021
Terminated at Mon Apr  5 18:32:50 2021
Results reported at Mon Apr  5 18:32:50 2021

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

    CPU time :                                   57162.18 sec.
    Max Memory :                                 8540 MB
    Average Memory :                             5900.88 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7844.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57323 sec.
    Turnaround time :                            57324 sec.

The output (if any) is above this job summary.

