
# Parameters

    Name :                      ReTest8-0
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
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      72489945284 function calls (72225330997 primitive calls) in 86109.19 seconds

##    Ordered by: cumulative time
   List reduced from 503 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.189 86109.189 {built-in method builtins.exec}
                      1    3.883    3.883 86109.189 86109.189 <string>:1(<module>)
                      1  333.208  333.208 86105.306 86105.306 main.py:75(CFagent)
                9886071   37.209    0.000 29963.682    0.003 agent.py:29(learn)
                9885203  679.307    0.000 24842.871    0.003 learner.py:42(Qlearn)
                3295357   14.675    0.000 21249.134    0.006 game.py:41(step)
                3295357   19.616    0.000 20438.189    0.006 layers.py:718(step)
                3295357  304.353    0.000 13727.146    0.004 layers.py:17(step)
              329130881  990.817    0.000 13393.445    0.000 layer.py:98(move)
                3295357  114.063    0.000 11591.797    0.004 agent.py:54(_learn)
        297647301/33034705 1185.621    0.000 11466.995    0.000 module.py:715(_call_impl)
                3295357  112.733    0.000 10731.903    0.003 agent.py:202(_learn)
               23149502   54.824    0.000 10708.407    0.000 network.py:24(forward)
               23149502  278.847    0.000 10510.949    0.000 container.py:115(forward)
                9885203   61.940    0.000 10143.532    0.001 grad_mode.py:23(decorate_context)
                9885203  338.475    0.000 9967.468    0.001 adam.py:55(step)
              329130881 1574.524    0.000 8230.803    0.000 layers.py:735(check)
                9885203 1834.296    0.000 8189.755    0.001 functional.py:53(adam)
                3295357 1055.610    0.000 7847.671    0.002 agent.py:210(counterfact)
                3295357   93.016    0.000 7582.571    0.002 agent.py:117(_learn)
                3295358  507.074    0.000 6661.659    0.002 layers.py:684(update)
                9885203   59.336    0.000 5733.791    0.001 tensor.py:181(backward)
                3295357 4165.898    0.001 5675.387    0.002 replaybuffer.py:22(sample_data)
                9885203   36.922    0.000 5674.455    0.001 __init__.py:68(backward)
               52234165 5453.613    0.000 5453.613    0.000 {built-in method tensor}
                9885203 5407.368    0.001 5407.368    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               44645895   26.535    0.000 5235.899    0.000 game.py:37(board)
                3295357 3707.236    0.001 5194.537    0.002 replaybuffer.py:52(sample_data)
                6623942  155.941    0.000 4966.952    0.001 agent.py:49(__call__)
                3295357 1855.039    0.001 4319.476    0.001 agent.py:88(interveen)
               65907150 2439.680    0.000 4258.523    0.000 layer.py:151(update)
               46299004   82.373    0.000 3828.874    0.000 conv.py:422(forward)
               46299004   94.729    0.000 3710.693    0.000 conv.py:414(_conv_forward)
               46299004 3597.943    0.000 3597.943    0.000 {built-in method conv2d}
                3295357 1898.982    0.001 3550.947    0.001 replaybuffer.py:28(teleporter_save_data)
              329130881  687.443    0.000 3484.022    0.000 layers.py:729(isFree)
               62857792  143.039    0.000 3403.804    0.000 linear.py:92(forward)
               62857792  243.043    0.000 3188.098    0.000 functional.py:1669(linear)
                3295357 1590.318    0.000 3122.145    0.001 agent.py:67(modify)
             2956303812 2303.252    0.000 2796.578    0.000 layer.py:95(isFree)
               42868529 2642.899    0.000 2642.899    0.000 {built-in method cat}
              645829296 1553.069    0.000 2577.573    0.000 tensor.py:933(grad)
             1246936323  715.998    0.000 2473.140    0.000 {built-in method builtins.any}
               62857792 2236.380    0.000 2236.380    0.000 {built-in method addmm}
                9885203  208.924    0.000 2234.199    0.000 optimizer.py:167(zero_grad)
             6351299493 1230.100    0.000 1763.154    0.000 enum.py:646(__hash__)
                3295357 1150.199    0.000 1754.899    0.001 replaybuffer.py:58(CF_save_data)
                3294489   50.372    0.000 1714.142    0.001 agent.py:171(__call__)
              184522632 1661.875    0.000 1661.875    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              141561654 1645.358    0.000 1645.358    0.000 {built-in method clone}
                3295357   49.900    0.000 1607.029    0.000 agent.py:112(__call__)
                9919299   68.621    0.000 1485.818    0.000 agent.py:59(modify_board)
               86007294   73.509    0.000 1481.694    0.000 activation.py:713(forward)
               86007294  112.779    0.000 1408.184    0.000 functional.py:1292(leaky_relu)
              834003920  455.414    0.000 1377.727    0.000 overrides.py:1070(has_torch_function)
              184522632 1357.778    0.000 1357.778    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              329130881  993.303    0.000 1318.149    0.000 layers.py:77(check)
               33056038  181.984    0.000 1293.291    0.000 tensor.py:21(wrapped)
               86007294 1284.234    0.000 1284.234    0.000 {built-in method torch._C._nn.leaky_relu}
                3295357   56.488    0.000 1260.049    0.000 replaybuffer.py:18(stacker)
                3294489   54.169    0.000 1241.470    0.000 replaybuffer.py:48(stacker)
             3597097317 1021.754    0.000 1237.604    0.000 layers.py:700(<genexpr>)
              329130881  779.027    0.000 1210.253    0.000 layers.py:246(check)
              362591838  155.479    0.000 1191.266    0.000 {built-in method builtins.all}
              329130881  678.271    0.000 1111.793    0.000 layers.py:286(check)
             1385311006  378.946    0.000 1054.312    0.000 layers.py:690(<genexpr>)
             1011838431  991.351    0.000  991.351    0.000 layer.py:146(elements)
                2526953   32.594    0.000  990.361    0.000 layers.py:740(restart)
                9919299  952.754    0.000  952.754    0.000 {built-in method torch._C._nn.one_hot}
               92261316  952.451    0.000  952.451    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               92261316  888.742    0.000  888.742    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             8569039083  814.640    0.000  814.640    0.000 layer.py:91(positions)
               92261316  788.839    0.000  788.839    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              329130881  545.509    0.000  704.322    0.000 layers.py:62(check)
                2526953   15.194    0.000  701.451    0.000 level.py:8(__init__)
               92261316  680.445    0.000  680.445    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        7977659460/7977659457  518.317    0.000  640.225    0.000 {built-in method builtins.len}
                3295357  365.857    0.000  627.862    0.000 collector.py:46(collect)
              329535800  410.084    0.000  615.033    0.000 layers.py:113(isDone)
              329130881  361.325    0.000  575.084    0.000 layers.py:273(check)
              329130881  361.464    0.000  570.017    0.000 layers.py:313(check)
                2526953   92.409    0.000  554.472    0.000 levels.py:199(generate)
             6351337044  533.061    0.000  533.061    0.000 {built-in method builtins.hash}
               11644620  202.552    0.000  524.365    0.000 random.py:315(sample)
               92261316  520.179    0.000  520.179    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6623942  189.358    0.000  519.095    0.000 exploration.py:53(softmaxer)
             1763921008  418.665    0.000  512.554    0.000 overrides.py:1083(<genexpr>)
                9885203   13.801    0.000  501.336    0.000 loss.py:445(forward)
              154775442  491.905    0.000  491.905    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9885203   52.260    0.000  487.535    0.000 functional.py:2637(mse_loss)
                3295357   85.008    0.000  481.080    0.000 agent.py:277(counterfact_check)
              329130881  317.000    0.000  467.065    0.000 layers.py:48(check)
               23067499  443.364    0.000  443.364    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                6591170  432.142    0.000  432.142    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               62857792  418.914    0.000  418.914    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5053906   43.929    0.000  375.995    0.000 level.py:41(notUsed)
              329130881  251.428    0.000  364.986    0.000 layers.py:23(check)
              290203775  223.276    0.000  308.414    0.000 layer.py:126(remove)
             3635016083  304.160    0.000  304.160    0.000 {method 'random' of '_random.Random' objects}
               23067499  293.576    0.000  293.576    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9514998: <ReTest8_0> in cluster <dcc> Done

Job <ReTest8_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 14 13:58:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 13:58:26 2021
Terminated at Thu Apr 15 13:53:38 2021
Results reported at Thu Apr 15 13:53:38 2021

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

    CPU time :                                   85886.91 sec.
    Max Memory :                                 3297 MB
    Average Memory :                             3261.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13087.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86111 sec.
    Turnaround time :                            86252 sec.

The output (if any) is above this job summary.

