
# Parameters

    Name :                      ReTest7-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78927774258 function calls (78635992967 primitive calls) in 86112.96 seconds

##    Ordered by: cumulative time
   List reduced from 503 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.964 86112.964 {built-in method builtins.exec}
                      1    3.517    3.517 86112.964 86112.964 <string>:1(<module>)
                      1  341.438  341.438 86109.447 86109.447 main.py:75(CFagent)
               10932708   41.522    0.000 31409.493    0.003 agent.py:29(learn)
               10928809  720.980    0.000 26061.404    0.002 learner.py:42(Qlearn)
                3644236   15.963    0.000 21692.026    0.006 game.py:41(step)
                3644236   19.146    0.000 20829.996    0.006 layers.py:718(step)
                3644236  326.428    0.000 14317.845    0.004 layers.py:17(step)
              364116491 1078.737    0.000 13959.696    0.000 layer.py:98(move)
                3644236  121.788    0.000 12140.899    0.003 agent.py:54(_learn)
        328238121/36458521 1225.719    0.000 11989.671    0.000 module.py:715(_call_impl)
                3644236  119.936    0.000 11243.666    0.003 agent.py:202(_learn)
               25529712   58.975    0.000 11194.908    0.000 network.py:24(forward)
               25529712  303.375    0.000 10984.609    0.000 container.py:115(forward)
               10928809   67.018    0.000 10661.562    0.001 grad_mode.py:23(decorate_context)
               10928809  380.059    0.000 10478.916    0.001 adam.py:55(step)
               10928809 1940.594    0.000 8602.794    0.001 functional.py:53(adam)
              364116491 1723.224    0.000 8588.151    0.000 layers.py:735(check)
                3644236   98.914    0.000 7960.315    0.002 agent.py:117(_learn)
                3644236  623.016    0.000 7294.255    0.002 agent.py:210(counterfact)
                3644237  531.841    0.000 6465.445    0.002 layers.py:684(update)
               10928809   62.039    0.000 5971.435    0.001 tensor.py:181(backward)
               10928809   36.819    0.000 5909.396    0.001 __init__.py:68(backward)
               10928809 5630.685    0.001 5630.685    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54830683 5580.010    0.000 5580.010    0.000 {built-in method tensor}
               46473790   27.229    0.000 5354.273    0.000 game.py:37(board)
                3644236 3728.425    0.001 5306.218    0.001 replaybuffer.py:22(sample_data)
                7289172  163.003    0.000 5148.595    0.001 agent.py:49(__call__)
                3644236 3165.803    0.001 4717.134    0.001 replaybuffer.py:52(sample_data)
                3644236 1745.373    0.000 4311.789    0.001 agent.py:88(interveen)
               72884730 2435.736    0.000 4279.258    0.000 layer.py:151(update)
               51059424   83.415    0.000 4013.495    0.000 conv.py:422(forward)
               51059424  101.071    0.000 3893.444    0.000 conv.py:414(_conv_forward)
               51059424 3774.138    0.000 3774.138    0.000 {built-in method conv2d}
              364116491  764.061    0.000 3592.996    0.000 layers.py:729(isFree)
               69300664  149.810    0.000 3551.641    0.000 linear.py:92(forward)
               69300664  252.682    0.000 3328.827    0.000 functional.py:1669(linear)
                3644236 1742.940    0.000 3312.692    0.001 replaybuffer.py:28(teleporter_save_data)
                3644236 1645.217    0.000 3238.565    0.001 agent.py:67(modify)
             3514986134 2279.265    0.000 2828.935    0.000 layer.py:95(isFree)
               47356273 2767.741    0.000 2767.741    0.000 {built-in method cat}
              713997410 1617.613    0.000 2682.405    0.000 tensor.py:933(grad)
             1378301951  740.484    0.000 2499.842    0.000 {built-in method builtins.any}
               10928809  239.305    0.000 2359.891    0.000 optimizer.py:167(zero_grad)
               69300664 2337.971    0.000 2337.971    0.000 {built-in method addmm}
             7005264420 1280.475    0.000 1811.113    0.000 enum.py:646(__hash__)
                3640337   52.500    0.000 1796.092    0.000 agent.py:171(__call__)
              203999236 1735.195    0.000 1735.195    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3644236   50.145    0.000 1668.300    0.000 agent.py:112(__call__)
               94830376   82.251    0.000 1543.271    0.000 activation.py:713(forward)
               10933408   72.199    0.000 1522.831    0.000 agent.py:59(modify_board)
               94830376  120.054    0.000 1461.021    0.000 functional.py:1292(leaky_relu)
              128719742 1443.268    0.000 1443.268    0.000 {built-in method clone}
              203999236 1430.586    0.000 1430.586    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              921792433  477.152    0.000 1427.551    0.000 overrides.py:1070(has_torch_function)
              364116491 1047.264    0.000 1380.080    0.000 layers.py:77(check)
               36495329  194.063    0.000 1341.717    0.000 tensor.py:21(wrapped)
               94830376 1329.108    0.000 1329.108    0.000 {built-in method torch._C._nn.leaky_relu}
                3644236   59.916    0.000 1319.545    0.000 replaybuffer.py:18(stacker)
                3640337   56.640    0.000 1298.608    0.000 replaybuffer.py:48(stacker)
                3644236  798.360    0.000 1248.993    0.000 replaybuffer.py:58(CF_save_data)
             3978776989  993.908    0.000 1223.503    0.000 layers.py:700(<genexpr>)
              364116491  747.533    0.000 1174.297    0.000 layers.py:246(check)
              364116491  699.240    0.000 1136.709    0.000 layers.py:286(check)
             1109848009 1008.473    0.000 1008.473    0.000 layer.py:146(elements)
              101999618  998.234    0.000  998.234    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2716701   32.753    0.000  997.482    0.000 layers.py:740(restart)
               10933408  964.287    0.000  964.287    0.000 {built-in method torch._C._nn.one_hot}
              101999618  933.813    0.000  933.813    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              400919029  109.339    0.000  900.178    0.000 {built-in method builtins.all}
             9499158186  851.642    0.000  851.642    0.000 layer.py:91(positions)
              101999618  825.068    0.000  825.068    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              760677721  172.130    0.000  809.382    0.000 layers.py:690(<genexpr>)
              364116491  554.882    0.000  729.109    0.000 layers.py:62(check)
              101999618  711.281    0.000  711.281    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2716701   15.060    0.000  709.179    0.000 level.py:8(__init__)
        8796383976/8796383973  544.632    0.000  675.942    0.000 {built-in method builtins.len}
                3644236  383.696    0.000  657.033    0.000 collector.py:46(collect)
              364423700  421.165    0.000  631.225    0.000 layers.py:113(isDone)
              364116491  402.398    0.000  625.807    0.000 layers.py:313(check)
              364116491  382.697    0.000  589.011    0.000 layers.py:273(check)
                2716701   92.826    0.000  563.063    0.000 levels.py:199(generate)
              101999618  551.851    0.000  551.851    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12721874  205.279    0.000  541.664    0.000 random.py:315(sample)
             7005305891  530.646    0.000  530.646    0.000 {built-in method builtins.hash}
                7289172  194.958    0.000  530.519    0.000 exploration.py:53(softmaxer)
             1949380131  426.270    0.000  528.583    0.000 overrides.py:1083(<genexpr>)
               10928809   14.340    0.000  527.521    0.000 loss.py:445(forward)
               10928809   56.449    0.000  513.181    0.000 functional.py:2637(mse_loss)
                3644236   87.460    0.000  496.510    0.000 agent.py:277(counterfact_check)
              364116491  325.111    0.000  483.842    0.000 layers.py:48(check)
               25509652  461.467    0.000  461.467    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              143293487  460.442    0.000  460.442    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7286029  441.496    0.000  441.496    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               69300664  438.695    0.000  438.695    0.000 {method 't' of 'torch._C._TensorBase' objects}
              364116491  269.134    0.000  397.514    0.000 layers.py:23(check)
                5433402   44.740    0.000  381.036    0.000 level.py:41(notUsed)
             4021027085  315.346    0.000  315.346    0.000 {method 'random' of '_random.Random' objects}
               25509652  305.424    0.000  305.424    0.000 {built-in method sum}
             2796843345  303.080    0.000  303.080    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9514997: <ReTest7_0> in cluster <dcc> Done

Job <ReTest7_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 14 13:57:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 13:57:18 2021
Terminated at Thu Apr 15 13:52:37 2021
Results reported at Thu Apr 15 13:52:37 2021

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

    CPU time :                                   85891.07 sec.
    Max Memory :                                 3293 MB
    Average Memory :                             3229.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13091.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            86191 sec.

The output (if any) is above this job summary.

